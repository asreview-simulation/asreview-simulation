import json
import click


@click.command(
    "print-settings",
    help="Print settings",
    short_help="Print settings",
)
@click.option(
    "-p",
    "--pretty",
    "pretty",
    help="Pretty-print the settings",
    is_flag=True,
)
@click.pass_obj
def print_settings_subcommand(obj, pretty):
    d = obj.models.asdict()
    if pretty:
        click.echo(json.dumps(d, indent=4, sort_keys=True))
        return
    click.echo(json.dumps(d))
