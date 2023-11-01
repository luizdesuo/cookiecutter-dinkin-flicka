"""{{cookiecutter.friendly_name}}."""

# read version from installed package
from importlib.metadata import version
__version__ = version("{{ cookiecutter.__package_slug }}")

# populate package namespace
from {{ cookiecutter.__package_slug }}.{{ cookiecutter.__package_slug }} import *