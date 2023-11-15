import hyperopt
from asreview_simulation.api import PartialConfig


def draw_sample(pyll):
    sample = hyperopt.rand.pyll.stochastic.sample(pyll)
    return PartialConfig(abbr=sample["abbr"], params=sample["params"])
