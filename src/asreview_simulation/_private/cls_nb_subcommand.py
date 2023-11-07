import click
from asreview.models.classifiers import NaiveBayesClassifier
from asreview_simulation._private.cli_epilog import epilog


name = f"cls-{NaiveBayesClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Naive Bayes classifier",
    name=name,
    short_help="Naive Bayes classifier",
)
@click.option(
    "--alpha",
    "alpha",
    default=3.822,
    help="Additive (Laplace/Lidstone) smoothing parameter (0 for no smoothing).",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.pass_obj
def cls_nb_subcommand(obj, alpha, force):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.classifier.abbr = name
    obj.models.classifier.params = {
        "alpha": alpha,
    }
    obj.provided.classifier = True
