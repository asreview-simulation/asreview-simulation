import click


@click.command(name="b-triple", help="Use triple balancer")
@click.option("-a", "a", type=float, help="hyperparameter 'a'.")
@click.option("-alpha", "alpha", type=float, help="hyperparameter 'alpha'.")
@click.option("-b", "b", type=float, help="hyperparameter 'b'.")
@click.option("-beta", "beta", type=float, help="hyperparameter 'beta'.")
@click.option("-c", "c", type=float, help="hyperparameter 'c'.")
@click.option("-gamma", "gamma", type=float, help="hyperparameter 'gamma'.")
@click.option("-shuffle", "shuffle", type=bool, help="hyperparameter 'shuffle'.")
@click.pass_obj
def triple(obj, a, alpha, b, beta, c, gamma, shuffle):
    assert obj.provided.balancer is False, "Attempted reassignment of triple balancer"
    obj.balancer.model = "triple"
    obj.balancer.params = {
        "a": a,
        "alpha": alpha,
        "b": b,
        "beta": beta,
        "c": c,
        "gamma": gamma,
        "shuffle": shuffle
    }
    obj.provided.balancer = True
