import click


name = "random"


@click.command(name=f"s-{name}", help="Use random prior sampler")
@click.option("--n_included", "n_included", default=1, type=click.INT, help="hyperparameter 'n_included'.")
@click.option("--n_excluded", "n_excluded", default=1, type=click.INT, help="hyperparameter 'n_excluded'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the querier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def random_prior_sampler(obj, n_included, n_excluded, force):
    if not force:
        assert obj.provided.sampler is False, "Attempted reassignment of sampler"
    obj.sampler.model = name
    obj.sampler.params = {
        "n_included": n_included,
        "n_excluded": n_excluded
    }
    obj.provided.sampler = True
