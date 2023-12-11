import sys
if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points
from typing import List
from typing import TypeAlias


TAbbrs: TypeAlias = List[str]


def get_abbrs() -> TAbbrs:
    """
    Returns:

        A list of recognized model abbreviations.
    """
    my_abbrs = {
        "bal-double",
        "bal-simple",
        "bal-undersample",
        "clr-logistic",
        "clr-lstm-base",
        "clr-lstm-pool",
        "clr-nb",
        "clr-nn-2-layer",
        "clr-rf",
        "clr-svm",
        "fex-doc2vec",
        "fex-embedding-idf",
        "fex-embedding-lstm",
        "fex-sbert",
        "fex-tfidf",
        "ofn-none",
        "ofn-wss",
        "qry-cluster",
        "qry-max",
        "qry-max-random",
        "qry-max-uncertainty",
        "qry-random",
        "qry-uncertainty",
        "sam-handpicked",
        "sam-random",
        "stp-none",
        "stp-nq",
        "stp-rel",
    }
    group = "asreview_simulationcontrib.subcommands"
    try:
        other_subcommands = {e.load() for e in entry_points(group=group)}
    except Exception as e:
        print(
            f"Something went wrong loading a module from entrypoint group '{group}'. Th"
            + f"e error message was: {e}\nContinuing..."
        )
        other_subcommands = set()

    other_abbrs = {o.name for o in other_subcommands}
    return sorted(my_abbrs.union(other_abbrs))
