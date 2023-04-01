import click
from asreviewlib.classifiers import SvmClassifier


name = SvmClassifier.name


@click.command(name=f"c-{name}", help="Use Support Vecor Machine classifier")
@click.option("-gamma", "gamma", default="auto", type=str, help="hyperparameter 'auto'.")
@click.option("-class_weight", "class_weight", default=0.249, type=float, help="hyperparameter 'class_weight'.")
@click.option("-c", "c", default=15.4, type=float, help="hyperparameter 'c'.")
@click.option("-kernel", "kernel", default="linear", type=str, help="hyperparameter 'kernel'.")
@click.pass_obj
def svm_classifier(obj, gamma, class_weight, c, kernel):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "gamma": gamma,
        "class_weight": class_weight,
        "c": c,
        "kernel": kernel
    }
    obj.provided.classifier = True
