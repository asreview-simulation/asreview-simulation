import click
from asreviewlib.classifiers import NN2LayerClassifier
from .._epilog import epilog


name = NN2LayerClassifier.name


@click.command(epilog=epilog,
               help="Use 2-layer Neural Net classifier",
               name=f"cls:{name}")
@click.option("--batch_size", "batch_size",
              default=32,
              help="hyperparameter 'batch_size'.",
              show_default=True,
              type=click.INT)
@click.option("--dense_width", "dense_width",
              default=128,
              help="hyperparameter 'dense_width'.",
              show_default=True,
              type=click.INT)
@click.option("--epochs", "epochs",
              default=35,
              help="hyperparameter 'epochs'.",
              show_default=True,
              type=click.INT)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--learn_rate", "learn_rate",
              default=1.0,
              help="hyperparameter 'learn_rate'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--optimizer", "optimizer",
              default="rmsprop",
              help="hyperparameter 'optimizer'.",
              show_default=True,
              type=click.Choice(["rmsprop"]))
@click.option("--regularization", "regularization",
              default=0.01,
              help="hyperparameter 'regularization'.",
              show_default=True,
              type=click.FLOAT)
@click.option("--shuffle", "shuffle",
              help="hyperparameter 'shuffle'.",
              is_flag=True)
@click.option("--verbose", "verbose",
              default=0,
              help="hyperparameter 'verbose'.",
              show_default=True,
              type=click.INT)
@click.pass_obj
def nn_2_layer_classifier(obj, batch_size, dense_width, epochs, force, learn_rate,
                          optimizer, regularization, shuffle, verbose):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "batch_size": batch_size,
        "dense_width": dense_width,
        "epochs": epochs,
        "learn_rate": learn_rate,
        "optimizer": optimizer,
        "regularization": regularization,
        "shuffle": shuffle
    }
    obj.provided.classifier = True
