import click
from .._epilog import epilog


name = "handpicked"


@click.command(epilog=epilog,
               help="Use handpicked prior sampler.\n\nIDS: a comma separated string",
               name=f"sam:{name}",
               short_help="Use handpicked prior sampler")
@click.argument("ids",
                type=click.STRING)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def handpicked_prior_sampler(obj, force, ids):
    """
    IDS: comma separated string
    """
    if not force:
        assert obj.provided.sampler is False, "Attempted reassignment of sampler"

    try:
        ids_list_of_int = [int(elem.strip()) for elem in ids.split(",")]
    except ValueError as e:
        click.echo("\nProblem parsing required argument IDS in 's-handpicked'.\n")
        raise e

    obj.sampler.model = name
    obj.sampler.params = {
        "ids": ids_list_of_int
    }
    obj.provided.sampler = True
