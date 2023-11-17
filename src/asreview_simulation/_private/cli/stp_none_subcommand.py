import click
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.one_model_config import OneModelConfig


name = "stp-none"


@click.command(
    epilog=epilog,
    help="Configure the simulation to stop after evaluating all records, "
    + "regardless of the relevance of evaluated records.",
    name=name,
    short_help="No stopping rule",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the stopping configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def stp_none_subcommand(obj, force):
    if not force:
        assert obj.provided.stp is False, (
            "Attempted reassignment of stopping. Use the --force flag "
            + "if you mean to overwrite the stopping configuration from previous steps. "
        )
    params = {}
    obj.models.stp = OneModelConfig(abbr=name, params=params)
    obj.provided.stp = True
