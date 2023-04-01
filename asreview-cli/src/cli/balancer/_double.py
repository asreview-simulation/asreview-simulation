import click


@click.command()
@click.option("-a", "a", default=2.155, type=float, help="hyperparameter 'a'.")
@click.option("-alpha", "alpha", default=0.94, type=float, help="hyperparameter 'alpha'.")
@click.option("-b", "b", default=0.789, type=float, help="hyperparameter 'b'.")
@click.option("-beta", "beta", default=1.0, type=float, help="hyperparameter 'beta'.")
@click.pass_obj
def double(obj, a, alpha, b, beta):
    assert obj.balancer.model is None, "Attempted reassignment of triple balancer"
    obj.balancer.model = "double"
    obj.balancer.params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta
    }
