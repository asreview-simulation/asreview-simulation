import hyperopt
from asreview_simulation.api import PartialConfig


def draw_sample(pyll) -> dict[str, PartialConfig]:
    valid_keys = {"bal", "cls", "fex", "qry", "sam", "stp"}
    assert type(pyll) == dict, "Expected input argument pyll to be of type 'dict'."
    for key in pyll.keys():
        assert key in valid_keys, f"Unexpected key '{key}' in keys of input argument 'pyll'."
    sample = hyperopt.rand.pyll.stochastic.sample(pyll)
    d = {}
    for key in sample.keys():
        abbr = sample[key]["abbr"]
        params = sample[key]["params"]
        pair = {
            key: PartialConfig(abbr=abbr, params=params)
        }
        d.update(pair)
    return d

