import click
from asreviewlib.classifiers import SvmClassifier
from .._epilog import epilog


name = SvmClassifier.name


@click.command(epilog=epilog,
               help="Use Support Vector Machine classifier",
               name=f"cls:{name}")
@click.option("--c", "c",
              default=15.4,
              help="hyperparameter 'c'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--class_weight", "class_weight",
              default=0.249,
              help="hyperparameter 'class_weight'.",
              show_default=True,
              type=click.FLOAT)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--gamma", "gamma",
              default="auto",
              help="hyperparameter 'auto'.",
              show_default=True,
              type=click.Choice("auto"))
@click.option("--kernel", "kernel",
              default="linear",
              help="hyperparameter 'kernel'.",
              show_default=True,
              type=click.Choice(["linear"]))
@click.pass_obj
def svm_classifier(obj, c, class_weight, gamma, force, kernel):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "c": c,
        "class_weight": class_weight,
        "gamma": gamma,
        "kernel": kernel
    }
    obj.provided.classifier = True
