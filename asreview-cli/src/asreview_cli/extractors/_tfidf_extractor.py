import click
from asreviewlib.extractors import TfidfExtractor


name = TfidfExtractor.name


@click.command(name=f"e-{name}", help="Use TF-IDF extractor")
@click.option("--n_grams_max", "n_grams_max", default=1, type=click.INT, help="hyperparameter 'n_grams_max'.")
@click.option("--stop_words", "stop_words", default="english", type=click.STRING, help="hyperparameter 'stop_words'.")
@click.option("-f", "--force", "force", is_flag=True, help="Force setting the extractor configura" +
              "tion, even if that means overwriting a previous configuration.")
@click.pass_obj
def tfidf_extractor(obj, n_grams_max, stop_words, force):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "n_grams_max": n_grams_max,
        "stop_words": stop_words
    }
    obj.provided.extractor = True
