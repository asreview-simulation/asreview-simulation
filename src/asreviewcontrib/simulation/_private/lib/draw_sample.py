from typing import Dict
import hyperopt
from asreviewcontrib.simulation._private.lib.one_model_config import OneModelConfig


def draw_sample(pyll: Dict[str, hyperopt.base.pyll.Apply]) -> Dict[str, OneModelConfig]:
    valid_keys = {"bal", "cls", "fex", "ofn", "qry", "sam", "stp"}
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
