import hyperopt
from asreview_simulation._private.lib.model_config import ModelConfig


def draw_sample(pyll):
    sample = hyperopt.pyll.stochastic.sample(pyll)
    return ModelConfig(abbr=sample["abbr"], params=sample["params"])
