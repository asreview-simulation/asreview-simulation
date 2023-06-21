import click
from asreview.models.classifiers import NN2LayerClassifier
from .._epilog import epilog


name = NN2LayerClassifier.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use 2-layer Neural Net classifier",
    name=f"cls-{name}",
    short_help="2-layer Neural Net classifier",
)
@click.option(
    "--batch_size",
    "batch_size",
    default=32,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--dense_width",
    "dense_width",
    default=128,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--epochs",
    "epochs",
    default=35,
    help="hyperparameter",
    show_default=True,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me"
    + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--learn_rate",
    "learn_rate",
    default=1.0,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--optimizer",
    "optimizer",
    default="rmsprop",
    help="hyperparameter",
    show_default=True,
    type=click.Choice(["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
)
@click.option(
    "--regularization",
    "regularization",
    default=0.01,
    help="hyperparameter",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--shuffle",
    "shuffle",
    help="hyperparameter",
    is_flag=True,
)
@click.pass_obj
def nn_2_layer_classifier(
    obj,
    batch_size,
    dense_width,
    epochs,
    force,
    learn_rate,
    optimizer,
    regularization,
    shuffle,
):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.classifier.abbr = name
    obj.classifier.params = {
        "batch_size": batch_size,
        "dense_width": dense_width,
        "epochs": epochs,
        "learn_rate": learn_rate,
        "optimizer": optimizer,
        "regularization": regularization,
        "shuffle": shuffle,
    }
    obj.provided.classifier = True
