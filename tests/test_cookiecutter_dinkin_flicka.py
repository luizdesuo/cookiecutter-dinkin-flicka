""" Test module for cookiecutter template """

import pytest
import re
from binaryornot.check import is_binary


PATTERN = r"{{(\s?cookiecutter)[.](.*?)}}"
RE_OBJ = re.compile(PATTERN)

@pytest.fixture
def context():
    return {
        "project_name": "my-test-project",
        "__package_slug": "my_test_project",
        "friendly_name": "My Test Project",
        "package_short_description": "A short description of the project.",
        "python_version": "3.11",
        "package_version": "0.0.0",
        "copyright_year": "2023",
        "author_name": "Test Author",
        "email": "test@example.com",
        "github_user": "authorgithub"
    }


SUPPORTED_COMBINATIONS = [
    {"license": "MIT"},
    {"license": "Apache License 2.0"},
    {"license": "GNU General Public License v3.0"},
    {"license": "BSD 3-Clause"},
    {"license": "Proprietary"},
    {"license": "None"},
    {"development_status": "Development Status :: 1 - Planning"},
    {"development_status": "Development Status :: 2 - Pre-Alpha"},
    {"development_status": "Development Status :: 3 - Alpha"},
    {"development_status": "Development Status :: 4 - Beta"},
    {"development_status": "Development Status :: 5 - Production/Stable"},
    {"development_status": "Development Status :: 6 - Mature"},
    {"development_status": "Development Status :: 7 - Inactive"},
    {"development_status": "None"},
    {"data_version_control": False},
    {"data_version_control": True},
    {"defensive_programming": False},
    {"defensive_programming": True},
    {"publish": False},
    {"publish": True},
]


def _fixture_id(ctx):
    """Helper to get a user-friendly test name from the parametrized context."""
    return "-".join(f"{key}:{value}" for key, value in ctx.items())


def build_paths_list(base_dir):
    """Build a list containing absolute paths to the generated files."""
    return [file_path for file_path in base_dir.rglob('*') if file_path.is_file()]

def check_paths(paths):
    """Method to check all paths have correct substitutions."""
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(str(path)):
            continue

        with path.open() as file:
            for line in file:
                match = RE_OBJ.search(line)
                assert match is None, f"cookiecutter variable not replaced in {path}"


@pytest.mark.parametrize("context_override", SUPPORTED_COMBINATIONS, ids=_fixture_id)
def test_project_generation(cookies, context, context_override):
    """Test that project is generated and fully rendered."""

    result = cookies.bake(extra_context={**context, **context_override})
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == context["project_name"]
    assert result.project_path.is_dir()

    paths = build_paths_list(result.project_path)
    assert paths
    check_paths(paths)

@pytest.mark.parametrize("license",
                         [
                             "MIT",
                             "Apache License 2.0",
                             "GNU General Public License v3.0",
                             "BSD 3-Clause",
                             "Proprietary"
                        ]
                    )
def test_dynamic_files_generated(cookies, context, license):
    """Ensures that dynamic files are generated."""
    context.update({"license": license})
    result = cookies.bake(extra_context=context)

    paths = build_paths_list(result.project_path)

    files = [path.name for path in paths]

    dynamic_files = [
        'LICENSE',
        'license.md'
    ]

    for dynamic_file in dynamic_files:
        assert dynamic_file in files

@pytest.mark.parametrize("license",
                         [
                             "None"
                        ]
                    )
def test_no_license(cookies, context, license):
    """Ensures that dynamic files are generated."""
    context.update({"license": license})
    result = cookies.bake(extra_context=context)

    paths = build_paths_list(result.project_path)

    files = [path.name for path in paths]

    dynamic_files = [
        'LICENSE',
        'license.md'
    ]

    for dynamic_file in dynamic_files:
        assert dynamic_file not in files