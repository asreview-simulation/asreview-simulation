from typing import Dict
import hyperopt
from asreviewcontrib.simulation._private.lib.config import OneModelConfig


def draw_sample(pyll: Dict[str, hyperopt.base.pyll.Apply]) -> Dict[str, OneModelConfig]:
    """
    Args:
        pyll:
            The Pyll program `dict`.

    Returns:

        A dictionary with model type abbreviation for each key (`bal`, `fex`,
        `stp`, etc), and the corresponding parameterization as randomly drawn
        by `hyperopt.rand.pyll.stochastic.sample`.

    Synopsis:

        Convenience function around `hyperopt.rand.pyll.stochastic.sample` to draw
        a random sample given a Pyll program `dict`, i.e. input argument `pyll`. The returned
        object can be directly passed into `Config`'s constructor by using keyword unpacking
        `**`, for example like so:

        ```python
        from asreviewcontrib.simulation.api import Config
        from asreviewcontrib.simulation.api import draw_sample
        from asreviewcontrib.simulation.api import get_pyll
        from asreviewcontrib.simulation.api import OneModelConfig


        fixed = {
            "ofn": OneModelConfig(abbr="ofn-wss", params={"at_pct": 90}),
            "qry": OneModelConfig(abbr="qry-max", params={"n_instances": 10}),
        }

        pyll = {
            "bal": get_pyll("bal-double"),
            "fex": get_pyll("fex-tfidf"),
        }

        # use pyll programs to draw a parameterization for 'bal' and 'fex'
        drawn = draw_sample(pyll)

        # construct an all-model config from one-model configs -- implicitly use default
        # model choice and parameterization for models not included as argument
        config = Config(**fixed, **drawn)
        ```
    """
    valid_keys = {"bal", "clr", "fex", "ofn", "qry", "sam", "stp"}
    assert isinstance(pyll, dict), "Expected input argument pyll to be of type 'dict'."
    for key in pyll.keys():
        assert key in valid_keys, f"Unexpected key '{key}' in keys of input argument 'pyll'."
    sample = hyperopt.rand.pyll.stochastic.sample(pyll)
    d = {}
    for key in sample.keys():
        abbr = sample[key]["abbr"]
        params = sample[key]["params"]
        pair = {
            key: OneModelConfig(abbr=abbr, params=params),
        }
        d.update(pair)
    return d
