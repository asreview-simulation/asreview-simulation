import hyperopt
from asreview_simulation._private.lib.config import PartialConfig


def draw_sample(pyll) -> PartialConfig:
    sample = hyperopt.pyll.stochastic.sample(pyll)
    return PartialConfig(abbr=sample["abbr"], params=sample["params"])
