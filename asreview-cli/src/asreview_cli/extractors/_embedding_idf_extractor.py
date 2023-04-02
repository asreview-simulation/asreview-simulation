import click
from asreviewlib.extractors import EmbeddingIdfExtractor


name = EmbeddingIdfExtractor.name


@click.command(name=f"e-{name}", help="Use Embedding IDF extractor")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the extractor configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def embedding_idf_extractor(obj, force):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {}
    obj.provided.extractor = True
