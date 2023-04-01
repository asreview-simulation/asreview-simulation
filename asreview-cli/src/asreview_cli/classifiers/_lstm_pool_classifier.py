import click
from asreviewlib.classifiers import LstmPoolClassifier


name = LstmPoolClassifier.name


@click.command(name=f"c-{name}", help="Use LSTM Pool classifier")
@click.pass_obj
def lstm_pool_classifier(obj):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.classifier = True
