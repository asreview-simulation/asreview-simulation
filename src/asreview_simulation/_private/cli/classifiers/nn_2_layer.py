import click
from asreview.models.classifiers import NN2LayerClassifier
from asreview_simulation._private.cli.epilog import epilog


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
    help="Batch size used for the neural network.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=30.0,
    help="Class weights for inclusions (1's).",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--dense_width",
    "dense_width",
    default=128,
    help="Size of the dense layers.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--epochs",
    "epochs",
    default=35,
    help="Number of epochs to train the neural network.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--learn_rate",
    "learn_rate",
    default=1.0,
    help="Learning rate multiplier of the default learning rate.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--optimizer",
    "optimizer",
    default="rmsprop",
    help="Name of the Keras optimizer.",
    show_default=True,
    type=click.Choice(["sgd", "rmsprop", "adagrad", "adam", "nadam"]),
)
@click.option(
    "--regularization",
    "regularization",
    default=0.01,
    help="Strength of the regularization on the weights and biases.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--shuffle",
    "shuffle",
    help="Whether to shuffle the training data prior to training.",
    is_flag=True,
)
@click.pass_obj
def cls_nn_2_layer(
    obj,
    batch_size,
    class_weight,
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
        "class_weight": class_weight,
        "dense_width": dense_width,
        "epochs": epochs,
        "learn_rate": learn_rate,
        "optimizer": optimizer,
        "regularization": regularization,
        "shuffle": shuffle,
    }
    obj.provided.classifier = True
