import click
from asreviewlib.balancers import TripleBalancer


name = TripleBalancer.name 


@click.command(name=f"b-{name}", help="Use triple balancer")
@click.option("--a", "a", default=2.155, type=click.FLOAT, help="hyperparameter 'a'.")
@click.option("--alpha", "alpha", default=0.94, type=click.FLOAT, help="hyperparameter 'alpha'.")
@click.option("--b", "b", default=0.789, type=click.FLOAT, help="hyperparameter 'b'.")
@click.option("--beta", "beta", default=1.0, type=click.FLOAT, help="hyperparameter 'beta'.")
@click.option("--c", "c", default=0.835, type=click.FLOAT, help="hyperparameter 'c'.")
@click.option("--gamma", "gamma", default=2.0, type=click.FLOAT, help="hyperparameter 'gamma'.")
@click.option("--shuffle", "shuffle", default=True, type=click.BOOL, help="hyperparameter 'shuffle'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the balancer configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def triple_balancer(obj, a, alpha, b, beta, c, gamma, shuffle, force):
    if not force:
        assert obj.provided.balancer is False, "Attempted reassignment of balancer"
    obj.balancer.model = name
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
