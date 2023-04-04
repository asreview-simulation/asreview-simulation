import click
from asreviewlib.extractors import TfidfExtractor
from .._epilog import epilog


name = TfidfExtractor.name


@click.command(epilog=epilog,
               help="Use TF-IDF extractor",
               name=f"ext:{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--ngram_max", "ngram_max",
              default=1,
              help="hyperparameter 'ngram_max'.",
              show_default=True,
              type=click.INT)
@click.option("--stop_words", "stop_words",
              default="english",
              help="hyperparameter 'stop_words'.",
              show_default=True,
              type=click.Choice(["english"]))
@click.pass_obj
def tfidf_extractor(obj, force, ngram_max, stop_words):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "ngram_max": ngram_max,
        "stop_words": stop_words
    }
    obj.provided.extractor = True
