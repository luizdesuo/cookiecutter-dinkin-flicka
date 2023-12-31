# Contributor Guide

Thank you for your interest in improving this project.
{% if cookiecutter.license != 'None' -%}
This project is open-source under the [{{cookiecutter.license.replace("-", " ")}} license] and
welcomes contributions in the form of bug reports, feature requests, and pull requests.
{% endif -%}

Here is a list of important resources for contributors:

- [Source Code]
- [Documentation]
- [Issue Tracker]
- [Code of Conduct]

{% if cookiecutter.license != 'None' -%}
[{{cookiecutter.license.replace("-", " ").lower()}} license]: https://opensource.org/licenses/{{cookiecutter.license}}
{% endif -%}
[source code]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}
{% if cookiecutter.publish -%}
[documentation]: https://{{cookiecutter.project_name}}.readthedocs.io/
{% endif -%}
[issue tracker]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/issues

## How to report a bug

Report bugs on the [Issue Tracker].

When filing an issue, make sure to answer these questions:

- Which operating system and Python version are you using?
- Which version of this project are you using?
- What did you do?
- What did you expect to see?
- What did you see instead?

The best way to get your bug fixed is to provide a test case,
and/or steps to reproduce the issue.

## How to request a feature

Request features on the [Issue Tracker].

## How to set up your development environment

You need Python 3.11+ and the following tools:

- [Poetry]
- [Nox]
- [Python Semantic Release]
- [Pre-commit]

Install the package with development requirements:

```bash
poetry install
```

You can now run an interactive Python session,
or the command-line interface:

```bash
poetry run python
poetry run {{cookiecutter.project_name}}
```

[poetry]: https://python-poetry.org/
[nox]: https://nox.thea.codes/
[Python Semantic Release]: https://python-semantic-release.readthedocs.io/
[Pre-commit]: https://pre-commit.com/



## How to test the project

Run the full test suite:

```bash
nox
```

List the available Nox sessions:

```bash
nox --list-sessions
```

You can also run a specific Nox session.
For example, invoke the unit test suite like this:

```bash
nox --session=tests
```

Unit tests are located in the _tests_ directory,
and are written using the [pytest] testing framework.

[pytest]: https://pytest.readthedocs.io/

## How to submit changes

Open a [pull request] to submit changes to this project.

Your pull request needs to meet the following guidelines for acceptance:

- The Nox test suite must pass without errors and warnings.
- Include unit tests. This project maintains 100% code coverage.
- If your changes add functionality, update the documentation accordingly.

Feel free to submit early, though—we can always iterate on this.

To run linting and code formatting checks before committing your change, you can install pre-commit as a Git hook by running the following command:

```bash
pre-commit install
```

The pre-commit hooks' versions can be updated by running the following command:

```bash
pre-commit autoupdate
```


It is recommended to open an issue before starting work on anything.
This will allow a chance to talk it over with the owners and validate your approach.

[pull request]: https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/pulls

<!-- github-only -->

[code of conduct]: CODE_OF_CONDUCT.md
