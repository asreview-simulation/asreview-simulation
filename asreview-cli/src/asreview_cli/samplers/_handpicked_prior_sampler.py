import click


name = "handpicked"


@click.command(name=f"s-{name}", help="Use handpicked prior sampler\n\n   IDS: a comma separated string")
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
    obj.sampler.model = name
    obj.sampler.params = {
        "ids": [int(elem.strip()) for elem in ids.split(",")]
    }
    obj.provided.sampler = True
