import click
from asreviewlib.extractors import SbertExtractor
from .._epilog import epilog


name = SbertExtractor.name


@click.command(epilog=epilog,
               help="Use SBERT extractor",
               name=f"ext:{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--transformer_model", "transformer_model",
              default="all-mpnet-base-v2",
              help="hyperparameter 'transformer_model'.",
              show_default=True,
              type=click.Choice(["all-mpnet-base-v2"]))
@click.pass_obj
def sbert_extractor(obj, force, transformer_model):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.extractor.model = name
    obj.extractor.params = {
        "transformer_model": transformer_model
    }
    obj.provided.extractor = True
