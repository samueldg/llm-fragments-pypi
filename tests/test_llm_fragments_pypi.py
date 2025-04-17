import json

import llm_fragments_pypi


def test_pypi_package_metadata_loader_no_version():
    fragments = llm_fragments_pypi.pypi_package_metadata_loader("llm")
    assert len(fragments) == 3

    # Check info fragment
    info_fragment = next(f for f in fragments if f.source == "pypi:llm/info")
    info_data = json.loads(str(info_fragment))
    assert info_data["name"] == "llm"
    assert isinstance(info_data["version"], str)  # Version might change over time
    assert "description" not in info_data
    assert "license" not in info_data
    assert "bugtrack_url" not in info_data
    assert "downloads" not in info_data
    assert "author" in info_data
    assert "home_page" in info_data

    # Check description fragment
    desc_fragment = next(f for f in fragments if f.source == "pypi:llm/description")
    assert str(desc_fragment)  # Should have some content
    assert len(str(desc_fragment)) > 0

    # Check license fragment
    license_fragment = next(f for f in fragments if f.source == "pypi:llm/license")
    assert str(license_fragment)  # Should have some content
    assert len(str(license_fragment)) > 0


def test_pypi_package_metadata_loader_with_version():
    fragments = llm_fragments_pypi.pypi_package_metadata_loader("llm@0.24")
    assert len(fragments) == 3

    # Check info fragment
    info_fragment = next(f for f in fragments if f.source == "pypi:llm@0.24/info")
    info_data = json.loads(str(info_fragment))
    assert info_data["name"] == "llm"
    assert info_data["version"] == "0.24"
    assert "description" not in info_data
    assert "license" not in info_data
    assert "bugtrack_url" not in info_data
    assert "downloads" not in info_data
    assert "author" in info_data
    assert "home_page" in info_data

    # Check description fragment
    desc_fragment = next(f for f in fragments if f.source == "pypi:llm@0.24/description")
    assert str(desc_fragment)  # Should have some content
    assert len(str(desc_fragment)) > 0

    # Check license fragment
    license_fragment = next(f for f in fragments if f.source == "pypi:llm@0.24/license")
    assert str(license_fragment)  # Should have some content
    assert len(str(license_fragment)) > 0
