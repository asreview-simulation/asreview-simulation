import click
from asreviewlib.extractors import Doc2VecExtractor


name = Doc2VecExtractor.name


@click.command(name=f"e-{name}", help="Use Doc2Vec extractor")
@click.option("-vector_size", "vector_size", default=40, type=int, help="hyperparameter 'vector_size'.")
@click.option("-epochs", "epochs", default=33, type=int, help="hyperparameter 'epochs'.")
@click.option("-min_count", "min_count", default=1, type=int, help="hyperparameter 'min_count'.")
@click.option("-n_jobs", "n_jobs", default=1, type=int, help="hyperparameter 'n_jobs'.")
@click.option("-window", "window", default=7, type=int, help="hyperparameter 'window'.")
@click.option("-dm_concat", "dm_concat", default=0, type=int, help="hyperparameter 'dm_concat'.")
@click.option("-dm", "dm", default=2, type=int, help="hyperparameter 'dm'.")
@click.option("-dbow_words", "dbow_words", default=0, type=int, help="hyperparameter 'dbow_words'.")
@click.pass_obj
def doc2vec_extractor(obj, vector_size, epochs, min_count, n_jobs, window, dm_concat, dm, dbow_words):
    assert obj.provided.extractor is False, "Attempted reassignment of extractor"
    obj.classifier.model = name
    obj.classifier.params = {
        "vector_size": vector_size,
        "epochs": epochs,
        "min_count": min_count,
        "n_jobs": n_jobs,
        "window": window,
        "dm_concat": dm_concat,
        "dm": dm,
        "dbow_words": dbow_words
    }
    obj.provided.extractor = True
