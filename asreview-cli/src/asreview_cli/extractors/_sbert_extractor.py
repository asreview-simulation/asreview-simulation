import click
from asreviewlib.extractors import SbertExtractor


name = SbertExtractor.name


@click.command(name=f"e-{name}", help="Use SBERT extractor")
@click.option("-transformer_model", "transformer_model", default="all-mpnet-base-v2", type=str,
              help="hyperparameter 'transformer_model'.")
@click.pass_obj
def sbert_extractor(obj, transformer_model):
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "transformer_model": transformer_model
    }
    obj.provided.extractor = True
