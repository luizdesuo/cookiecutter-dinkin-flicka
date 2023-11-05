# {{ cookiecutter.friendly_name }}

{{ cookiecutter.package_short_description }}

{% if cookiecutter.publish -%}
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.project_name}}.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/{{cookiecutter.project_name}}.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}})][pypi status]
[![License](https://img.shields.io/pypi/l/{{cookiecutter.project_name}})][license]

[![Read the documentation at https://{{cookiecutter.project_name}}.readthedocs.io/](https://img.shields.io/readthedocs/{{cookiecutter.project_name}}/latest.svg?label=Read%20the%20Docs)][read the docs]
{% endif -%}
[![Release](https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/workflows/release/badge.svg)][release]
[![Codecov](https://codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

{% if cookiecutter.publish -%}
[pypi status]: https://pypi.org/project/{{cookiecutter.project_name}}/
[read the docs]: https://{{cookiecutter.project_name}}.readthedocs.io/
{% endif -%}
[release]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/actions?workflow=release
[codecov]: https://app.codecov.io/gh/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

- TODO

## Requirements

- TODO

## Installation

{% if cookiecutter.publish -%}
You can install _{{cookiecutter.friendly_name}}_ via [pip] from [PyPI]:

```bash
pip install {{cookiecutter.project_name}}
```

{% else -%}
You can install _{{cookiecutter.friendly_name}}_ via github:

```bash
pip install git+ssh://git@github.com:{{cookiecutter.github_user}}/{{cookiecutter.project_name}}.git -vvv
```

{% endif -%}

## Usage

Please see the [Command-line Reference] for details.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

{% if cookiecutter.license != 'None' -%}
## License

Distributed under the terms of the [{{cookiecutter.license.replace("-", " ")}} license][license],
_{{cookiecutter.friendly_name}}_ is free and open source software.
{% endif -%}

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [Dinkin Flicka Cookiecutter] template.

[pypi]: https://pypi.org/
[dinkin flicka cookiecutter]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka
[file an issue]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

{% if cookiecutter.license != 'None' -%}
[license]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/LICENSE
{% endif -%}
[contributor guide]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/blob/main/CONTRIBUTING.md
{% if cookiecutter.publish -%}
[command-line reference]: https://{{cookiecutter.project_name}}.readthedocs.io/en/latest/usage.html
{% endif -%}