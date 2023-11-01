import click
from asreview.models.feature_extraction import Doc2Vec
from .._epilog import epilog


name = Doc2Vec.name


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Doc2Vec extractor.",
    name=f"fex-{name}",
    short_help="Doc2Vec extractor",
)
@click.option(
    "--dbow_words",
    "dbow_words",
    default=0,
    help="Whether to train the word vectors using the skipgram method.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--dm",
    "dm",
    default="both",
    help="Model to use. 'dbow': Use distribute bag of words; 'dm': Use distributed memory; "
    + "'both': Use both 'dbow' and 'dm' with half the vector size and concatenate them.",
    show_default=True,
    type=click.Choice(["dbow", "dm", "both"]),
)
@click.option(
    "--dm_concat",
    "dm_concat",
    default=0,
    help="Whether to concatenate word vectors or not.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--epochs",
    "epochs",
    default=33,
    help="Number of epochs to train the doc2vec model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--min_count",
    "min_count",
    default=1,
    help="Minimum number of occurences for a word in the corpus for it to be included in the model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    help="hyperparameter",
)
@click.option(
    "--use_keywords",
    "use_keywords",
    help="hyperparameter",
)
@click.option(
    "--vector_size",
    "vector_size",
    default=40,
    help="Output size of the vector.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--window",
    "window",
    default=7,
    help="Maximum distance over which word vectors influence each other.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def doc2vec_extractor(
    obj,
    dbow_words,
    dm,
    dm_concat,
    epochs,
    force,
    min_count,
    split_ta,
    use_keywords,
    vector_size,
    window,
):
    if not force:
        assert obj.provided.extractor is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.extractor.abbr = name
    obj.extractor.params = {
        "dbow_words": dbow_words,
        "dm": {"dbow": 0, "dm": 1, "both": 2}[dm],
        "dm_concat": dm_concat,
        "epochs": epochs,
        "min_count": min_count,
        "split_ta": split_ta,
        "use_keywords": use_keywords,
        "vector_size": vector_size,
        "window": window,
    }
    obj.provided.extractor = True
