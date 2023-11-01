# Dinkin Flicka

a versatile cookiecutter template for python projects

<!-- badges-begin -->

[![PyPI](https://img.shields.io/pypi/v/cookiecutter-dinkin-flicka.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/cookiecutter-dinkin-flicka.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/cookiecutter-dinkin-flicka)][pypi status]
[![License](https://img.shields.io/pypi/l/cookiecutter-dinkin-flicka)][license]

[![Read the documentation at https://cookiecutter-dinkin-flicka.readthedocs.io/](https://img.shields.io/readthedocs/cookiecutter-dinkin-flicka/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Release](https://github.com/luizdesuo/cookiecutter-dinkin-flicka/workflows/release/badge.svg)][release]
[![Codecov](https://codecov.io/gh/luizdesuo/cookiecutter-dinkin-flicka/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/cookiecutter-dinkin-flicka/
[read the docs]: https://cookiecutter-dinkin-flicka.readthedocs.io/
[release]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka/actions?workflow=release
[codecov]: https://app.codecov.io/gh/luizdesuo/cookiecutter-dinkin-flicka
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

<!-- badges-end -->

<p align="center"><img alt="logo" src="docs/_static/logo.png" width="25%" /></p>

<!-- docs-only -->

## Installation

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

    ```bash
    pip install cookiecutter
    ```

2. Generate a Python package structure using [`cookiecutter-dinkin-flicka`](https://github.com/luizdesuo/cookiecutter-dinkin-flicka.git):

    ```bash
    cookiecutter https://github.com/luizdesuo/cookiecutter-dinkin-flicka.git
    ```

## Usage

Enter the settings:

* project_name
* friendly_name
* package_short_description
* python_version
* package_version
* copyright_year
* author
* email
* github_user
* license
    1. MIT
    2. Apache License 2.0
    3. GNU General Public License v3.0
    4. BSD 3-Clause
    5. Proprietary
    6. None
* development_status
    1. Development Status :: 1 - Planning
    2. Development Status :: 2 - Pre-Alpha
    3. Development Status :: 3 - Alpha
    4. Development Status :: 4 - Beta
    5. Development Status :: 5 - Production/Stable
    6. Development Status :: 6 - Mature
    7. Development Status :: 7 - Inactive
    8. None
* data_version_control: include [dvc], [pandas], [pyjanitor] and [pandera]
    1. false
    2. true
* defensive_programming: include [icontract], [hypothesis], [icontract-hypothesis]
    1. false
    2. trueee
* publish: include [pypi] and [testpypi] publishing into github workflow
           in addition to [readthedocs] mentions into documentation
    1. false
    2. true

The project structure will look similar to that shown below:

```text
    project-name
    ├── bandit.yml
    ├── codecov.yml
    ├── CODE_OF_CONDUCT.md
    ├── CONTRIBUTING.md
    ├── .cookiecutter.json
    ├── .darglint
    ├── docs
    │   ├── codeofconduct.md
    │   ├── conf.py
    │   ├── contributing.md
    │   ├── index.md
    │   ├── license.md
    │   ├── requirements.txt
    │   └── usage.md
    ├── .editorconfig
    ├── .flake8
    ├── .gitattributes
    ├── .github
    │   ├── dependabot.yml
    │   └── workflows
    │       └── release.yml
    ├── .gitignore
    ├── LICENSE
    ├── noxfile.py
    ├── .pre-commit-config.yaml
    ├── pyproject.toml
    ├── README.md
    ├── .readthedocs.yml
    ├── src
    │   └── project_name
    │       ├── __init__.py
    │       ├── __main__.py
    │       ├── project_name.py
    │       └── py.typed
    └── tests
        ├── __init__.py
        ├── test_main.py
        └── test_project_name.py
```

Then, install the project with:

```bash
poetry install project-name
```

Start version control tracking:

```bash
git init
git add .
git commit -m "initial package setup"
```

Install the [pre-commit] hooks:

```bash
poetry run pre-commit install
```

Update the [pre-commit] hooks' versions:

```bash
poetry run pre-commit autoupdate
```

Finally, add to version control:

```bash
git add .pre-commit-config.yaml
```

And, commit:

```bash
git commit -m "build: update pre-commit hooks versions"
```

## Features

TODO

Please, check the [slides].

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Dinkin Flicka_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [Dinkin Flicka Cookiecutter] template.

[pypi]: https://pypi.org/
[dinkin flicka cookiecutter]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka
[file an issue]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka/issues
[pip]: https://pip.pypa.io/
[testpypi]: https://test.pypi.org/
[readthedocs]: https://about.readthedocs.com/
[dvc]: https://dvc.org/
[pandas]: https://pandas.pydata.org/
[pyjanitor]: https://pyjanitor-devs.github.io/pyjanitor/
[pandera]: https://pandera.readthedocs.io/en/latest/
[icontract]: https://icontract.readthedocs.io/en/latest/
[hypothesis]: https://hypothesis.works/
[icontract-hypothesis]: https://github.com/mristin/icontract-hypothesis
[slides]: https://luizdesuo.github.io/cookiecutter-dinkin-flicka/


<!-- github-only -->

[license]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka/blob/main/LICENSE
[contributor guide]: https://github.com/luizdesuo/cookiecutter-dinkin-flicka/blob/main/CONTRIBUTING.md
