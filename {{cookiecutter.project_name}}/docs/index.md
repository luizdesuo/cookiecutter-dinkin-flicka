```{include} ../README.md
---
end-before: <!-- github-only -->
---
```

{% if cookiecutter.license != 'None' -%}
[license]: license
{% endif -%}
[contributor guide]: contributing
[command-line reference]: usage

```{toctree}
---
hidden:
maxdepth: 1
---

usage
autoapi/index
contributing
Code of Conduct <codeofconduct>
{% if cookiecutter.license != 'None' -%}
License <license>
{% endif -%}
Changelog <https://github.com/{{cookiecutter.github_user}}/{{cookiecutter.project_name}}/releases>
```