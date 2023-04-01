import click


@click.command(name="b-undersample", help="Use undersample balancer")
@click.option("-ratio", "ratio", default=1.0, type=float, help="hyperparameter 'ratio'.")
@click.pass_obj
def undersample(obj, ratio):
    assert obj.provided.balancer is False, "Attempted reassignment of undersample balancer"
    obj.balancer.model = "undersample"
    obj.balancer.params = {
        "ratio": ratio
    }
    obj.provided.balancer = True
