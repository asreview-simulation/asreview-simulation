import click
from asreviewlib.extractors import EmbeddingIdfExtractor


name = EmbeddingIdfExtractor.name


@click.command(name=f"e-{name}", help="Use Embedding IDF extractor")
@click.pass_obj
def embedding_idf_extractor(obj):
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.extractor = True
