import click
from asreview.models.feature_extraction import Doc2Vec
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_fex_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.fex.fex_doc2vec_params import get_fex_doc2vec_params


default_params = get_fex_doc2vec_params()
name = f"fex-{Doc2Vec.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Doc2Vec extractor.",
    name=name,
    short_help="Doc2Vec extractor",
)
@click.option(
    "--dbow_words",
    "dbow_words",
    default=default_params["dbow_words"],
    help="Include this flag to train the word vectors using the skipgram method.",
    is_flag=True,
)
@click.option(
    "--dm",
    "dm",
    default=default_params["dm"],
    help="Model to use. 'dbow': Use distribute bag of words; 'dm': Use distributed memory; "
    + "'both': Use both 'dbow' and 'dm' with half the vector size and concatenate them.",
    show_default=True,
    type=click.Choice(["dbow", "dm", "both"]),
)
@click.option(
    "--dm_concat",
    "dm_concat",
    default=default_params["dm_concat"],
    help="Include this flag to concatenate word vectors.",
    is_flag=True,
)
@click.option(
    "--epochs",
    "epochs",
    default=default_params["epochs"],
    help="Number of epochs to train the doc2vec model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'fex' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--min_count",
    "min_count",
    default=default_params["min_count"],
    help="Minimum number of occurences for a word in the corpus for it to be included in the model.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    default=default_params["split_ta"],
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.option(
    "--vector_size",
    "vector_size",
    default=default_params["vector_size"],
    help="Output size of the vector.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--window",
    "window",
    default=default_params["window"],
    help="Maximum distance over which word vectors influence each other.",
    show_default=True,
    type=click.INT,
)
@click.pass_obj
def fex_doc2vec_subcommand(
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
        assert obj.provided.fex is False, dont_reassign_fex_msg
    params = {
        "dbow_words": dbow_words,
        "dm": dm,
        "dm_concat": dm_concat,
        "epochs": epochs,
        "min_count": min_count,
        "split_ta": split_ta,
        "use_keywords": use_keywords,
        "vector_size": vector_size,
        "window": window,
    }
    obj.config.fex = OneModelConfig(abbr=name, params=params)
    obj.provided.fex = True
