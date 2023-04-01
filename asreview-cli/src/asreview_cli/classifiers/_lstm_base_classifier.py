import click
from asreviewlib.classifiers import LstmBaseClassifier


name = LstmBaseClassifier.name


@click.command(name=f"c-{name}", help="Use LSTM Base classifier")
@click.pass_obj
def lstm_base_classifier(obj):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.classifier = True
