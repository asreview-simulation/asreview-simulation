import json
import click


@click.command(
    "save-settings",
    help="Save settings",
    short_help="Save settings",
)
@click.option(
    "--to",
    "filename",
    help="Where to save the settings",
    required=True,
    type=click.File("w"),
)
@click.option(
    "-p",
    "--pretty",
    "pretty",
    help="Pretty-print the settings",
    is_flag=True,
)
@click.pass_obj
def save_settings_subcommand(obj, filename, pretty):
    d = obj.models.asdict()
    if pretty:
        with filename as f:
            s = json.dumps(d, indent=4, sort_keys=True)
            f.write(s)
        return
    with filename as f:
        s = json.dumps(d)
        f.write(s)
