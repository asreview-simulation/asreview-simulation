import click
from asreviewlib.classifiers import LstmPoolClassifier
from .._epilog import epilog


name = LstmPoolClassifier.name


@click.command(epilog=epilog,
               help="Use LSTM Pool classifier",
               name=f"cls:{name}")
@click.argument("feature_matrix_file",
                type=click.Path(exists=True, readable=True))
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.pass_obj
def lstm_pool_classifier(obj, feature_matrix_file, force):
    if not force:
        assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.classifier = True
