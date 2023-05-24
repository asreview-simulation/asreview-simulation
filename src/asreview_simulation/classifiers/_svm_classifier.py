import click
from asreview.models.classifiers import SVMClassifier
from .._epilog import epilog


name = SVMClassifier.name


@click.command(epilog=epilog,
               help="Use Support Vector Machine classifier",
               name=f"cls:{name}")
@click.option("--c", "c",
              default=15.4,
              help="hyperparameter.",
              show_default=True,
              type=click.FLOAT)
@click.option("--class_weight", "class_weight",
              default=0.249,
              help="hyperparameter",
              show_default=True,
              type=click.FLOAT)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--gamma", "gamma",
              default="auto",
              help="hyperparameter",
              show_default=True,
              type=click.Choice(["auto", "scale"]))
@click.option("--kernel", "kernel",
              default="linear",
              help="hyperparameter",
              show_default=True,
              type=click.Choice(["linear", "rbf", "poly", "sigmoid"]))
@click.option("--seed", "seed",
              default=535,
              help="Random seed",
              show_default=True,
              type=click.INT)
@click.pass_obj
def svm_classifier(obj, c, class_weight, gamma, force, kernel, seed):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "c": c,
        "class_weight": class_weight,
        "gamma": gamma,
        "kernel": kernel,
        "seed": seed
    }
    obj.provided.classifier = True
