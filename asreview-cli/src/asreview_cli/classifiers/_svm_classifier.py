import click
from asreviewlib.classifiers import SvmClassifier
from .._epilog import epilog


name = SvmClassifier.name


@click.command(name=f"c-{name}", help="Use Support Vecor Machine classifier", epilog=epilog)
@click.option("--gamma", "gamma", default="auto", type=click.STRING, help="hyperparameter 'auto'.")
@click.option("--class_weight", "class_weight", default=0.249, type=click.FLOAT, help="hyperparameter 'class_weight'.")
@click.option("--c", "c", default=15.4, type=click.FLOAT, help="hyperparameter 'c'.")
@click.option("--kernel", "kernel", default="linear", type=click.STRING, help="hyperparameter 'kernel'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the classifier configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def svm_classifier(obj, gamma, class_weight, c, kernel, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "gamma": gamma,
        "class_weight": class_weight,
        "c": c,
        "kernel": kernel
    }
    obj.provided.classifier = True
