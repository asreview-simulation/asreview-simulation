import click
from asreview_simulation._private.cli_epilog import epilog
from asreview_simulation._private.sam.sam_handpicked_config import get_sam_handpicked_config


default_params = get_sam_handpicked_config().params
name = "sam-handpicked"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Handpicked prior sampler. IDS: a comma separated string",
    name=name,
    short_help="Handpicked prior sampler",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--records",
    "records",
    default=default_params["records"],
    help="Comma-separated string of integers, where each integer is the identifier for a record as used in the data.",
    type=click.STRING,
)
@click.option(
    "--rows",
    "rows",
    default=default_params["rows"],
    help="Comma-separated string of integers, where each integer is the row number of a record in the data.",
    type=click.STRING,
)
@click.pass_obj
def sam_handpicked_subcommand(obj, force, records, rows):
    if not force:
        assert obj.provided.sam is False, (
            "Attempted reassignment of sampler. Use the --force flag "
            + "if you mean to overwrite the sampler configuration from previous steps. "
        )

    assert not (rows is None and records is None), "Need to define either --rows or --records."
    assert not (rows is not None and records is not None), "Need to define one of --rows or --records, not both."

    obj.models.sam.abbr = name

    if rows is not None:
        try:
            ids = [int(elem.strip()) for elem in rows.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing row numbers.\n")
            raise e
        obj.models.sam.params = {
            "rows": ids,
        }

    if records is not None:
        try:
            ids = [int(elem.strip()) for elem in records.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing record numbers.\n")
            raise e
        obj.models.sam.params = {
            "records": ids,
        }

    obj.provided.sam = True
