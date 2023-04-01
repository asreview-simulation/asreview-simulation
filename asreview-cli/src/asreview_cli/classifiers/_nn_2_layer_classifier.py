import click
from asreviewlib.classifiers import NN2LayerClassifier


name = NN2LayerClassifier.name


@click.command(name=f"c-{name}", help="Use 2-layer Neural Net classifier")
@click.option("-dense_width", "dense_width", default=128, type=int, help="hyperparameter 'dense_width'.")
@click.option("-optimizer", "optimizer", default="rmsprop", type=str, help="hyperparameter 'optimizer'.")
@click.option("-learn_rate", "learn_rate", default=1.0, type=float, help="hyperparameter 'learn_rate'.")
@click.option("-regularization", "regularization", default=0.01, type=float, help="hyperparameter 'regularization'.")
@click.option("-verbose", "verbose", default=0, type=int, help="hyperparameter 'verbose'.")
@click.option("-epochs", "epochs", default=35, type=int, help="hyperparameter 'epochs'.")
@click.option("-batch_size", "batch_size", default=32, type=int, help="hyperparameter 'batch_size'.")
@click.option("-shuffle", "shuffle", default=False, type=bool, help="hyperparameter 'shuffle'.")
@click.pass_obj
def nn_2_layer_classifier(obj, dense_width, optimizer, regularization, verbose, epochs, shuffle):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "dense_width": dense_width,
        "optimizer": optimizer,
        "regularization": regularization,
        "verbose": verbose,
        "epochs": epochs,
        "shuffle": shuffle
    }
    obj.provided.classifier = True
