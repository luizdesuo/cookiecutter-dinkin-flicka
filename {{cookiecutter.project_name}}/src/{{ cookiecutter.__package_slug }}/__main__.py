"""Command-line interface."""
import click


@click.group()
@click.version_option()
def main() -> None:
    """{{cookiecutter.friendly_name}}."""

@main.command()
def hello() -> None:
    click.echo(f"Hello")


if __name__ == "__main__":
    main(prog_name="{{cookiecutter.project_name}}")  # pragma: no cover
