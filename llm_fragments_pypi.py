import json

import httpx
import llm

_PREFIX = "pypi"

_PYPI_JSON_API_HEADERS = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}


@llm.hookimpl
def register_fragment_loaders(register):
    register(_PREFIX, pypi_package_metadata_loader)


def pypi_package_metadata_loader(argument: str) -> list[llm.Fragment]:
    parts = argument.split("@", maxsplit=1)
    package_data = _get_pypi_package_metadata(*parts)

    # Only include top-level information
    # Other keys include releases and urls, which can be massive payloads
    # Larger fields are split into separate fragments
    package_info = package_data["info"]
    description = package_info.pop("description", "")
    license = package_info.pop("license", "")

    # Remove keys that are deprecated and return no or bad data
    # See warning in https://docs.pypi.org/api/json/#get-a-project
    del package_info["bugtrack_url"]
    del package_info["downloads"]

    fragments = {
        "info": json.dumps(package_info, indent=2),
        "description": description,
        "license": license,
    }
    return [llm.Fragment(content=text, source=f"{_PREFIX}:{argument}/{suffix}") for suffix, text in fragments.items()]


def _get_pypi_package_metadata(package_name: str, version: str | None = None) -> dict:
    """
    https://docs.pypi.org/api/json/
    """

    if version is None:
        package_url = f"https://pypi.org/pypi/{package_name}/json"
    else:
        package_url = f"https://pypi.org/pypi/{package_name}/{version}/json"

    response = httpx.get(package_url, headers=_PYPI_JSON_API_HEADERS)
    response.raise_for_status()
    return response.json()
