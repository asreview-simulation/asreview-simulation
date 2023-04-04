import click
from asreviewlib.extractors import Doc2VecExtractor
from .._epilog import epilog


name = Doc2VecExtractor.name


@click.command(epilog=epilog,
               help="Use Doc2Vec extractor",
               name=f"e-{name}")
@click.option("--epochs", "epochs",
              default=33,
              help="hyperparameter 'epochs'.",
              show_default=True,
              type=click.INT)
@click.option("--dbow_words", "dbow_words",
              default=0,
              help="hyperparameter 'dbow_words'.",
              show_default=True,
              type=click.INT)
@click.option("--dm", "dm",
              default=2,
              help="hyperparameter 'dm'.",
              show_default=True,
              type=click.INT)
@click.option("--dm_concat", "dm_concat",
              default=0,
              help="hyperparameter 'dm_concat'.",
              show_default=True,
              type=click.INT)
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--min_count", "min_count",
              default=1,
              help="hyperparameter 'min_count'.",
              show_default=True,
              type=click.INT)
@click.option("--n_jobs", "n_jobs",
              default=1,
              help="hyperparameter 'n_jobs'.",
              show_default=True,
              type=click.INT)
@click.option("--vector_size", "vector_size",
              default=40,
              help="hyperparameter 'vector_size'.",
              show_default=True,
              type=click.INT)
@click.option("--window", "window",
              default=7,
              help="hyperparameter 'window'.",
              show_default=True,
              type=click.INT)
@click.pass_obj
def doc2vec_extractor(obj, epochs, dbow_words, dm, dm_concat, force, min_count, n_jobs, vector_size, window):
    if not force:
        assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "dbow_words": dbow_words,
        "dm": dm,
        "dm_concat": dm_concat,
        "epochs": epochs,
        "min_count": min_count,
        "n_jobs": n_jobs,
        "vector_size": vector_size,
        "window": window
    }
    obj.provided.extractor = True
