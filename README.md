# llm-fragments-pypi

Load PyPI package metadata as LLM fragments.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

```sh
llm install llm-fragments-pypi
```

## Usage

Use `-f pypi:package_name` to include the package's README and metadata as fragments.

```sh
# Retrieve a package's latest version
llm -f pypi:polars "How does the performance of polars compare to pandas?"
```

You can optionally specify a version with the `@version` suffix:

```sh
# Retrieve a specific version
llm -f pypi:pydantic@1.6 "What are the Python versions supported by pydantic?"
```

You can combine multiple fragments:

```sh
llm -f pypi:litestar -f pypi:fastapi \
  "What are some similarities and differences between litestar and fastapi?"
```

## Development

### Local Setup

To set up this plugin locally, use `uv`:

```sh
uv run llm install -e .
```

It'll take care of creating a virtual environment, installing the dependencies,
and you can run a `uv run llm` instance that will use the local version of the plugin.

### Dev dependencies

Install the dev dependencies in your local environment:

```sh
uv sync --group dev
```

### Linting & formatting

You can format and lint the code with `ruff`:

```sh
uv run ruff format .
uv run ruff check .
```

And run the pre-commit hooks:

```sh
uv run pre-commit install
```

### Tests

Run tests:

```sh
uv run pytest
```
