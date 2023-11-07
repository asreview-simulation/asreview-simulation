import click
from asreview_simulation._private.cli_epilog import epilog


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
    default=None,
    help="Comma-separated string of integers, where each integer is the identifier for a record as used in the data.",
    type=click.STRING,
)
@click.option(
    "--rows",
    "rows",
    default=None,
    help="Comma-separated string of integers, where each integer is the row number of a record in the data.",
    type=click.STRING,
)
@click.pass_obj
def sam_handpicked_subcommand(obj, force, records, rows):
    if not force:
        assert obj.provided.sampler is False, (
            "Attempted reassignment of sampler. Use the --force flag "
            + "if you mean to overwrite the sampler configuration from previous steps. "
        )

    assert not (rows is None and records is None), "Need to define either --rows or --records."
    assert not (rows is not None and records is not None), "Need to define one of --rows or --records, not both."

    obj.models.sampler.abbr = name

    if rows is not None:
        try:
            ids = [int(elem.strip()) for elem in rows.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing row numbers.\n")
            raise e
        obj.models.sampler.params = {
            "rows": ids,
        }

    if records is not None:
        try:
            ids = [int(elem.strip()) for elem in records.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing record numbers.\n")
            raise e
        obj.models.sampler.params = {
            "records": ids,
        }

    obj.provided.sampler = True
