import click
from .._epilog import epilog


name = "handpicked"


@click.command(name=f"s-{name}", help="Use handpicked prior sampler\n\n   " +
               "IDS: a comma separated string", epilog=epilog)
@click.argument("ids", type=click.STRING)
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the querier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def handpicked_prior_sampler(obj, ids, force):
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
