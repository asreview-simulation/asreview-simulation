from typing import Dict
from typing import Optional
from asreview_simulation._private.lib.get_default_params import get_default_params


class OneModelConfig:
    def __init__(self, abbr: str, params: Optional[Dict] = None):
        assert isinstance(abbr, str), "Expected input argument 'abbr' to be of type 'str'"
        default_params = get_default_params(abbr)
        self.abbr = abbr
        self.params = default_params
        if params is not None:
            assert isinstance(params, dict), "Expected input argument 'params' to be of type 'dict'"
            valid_keys = default_params.keys()
            provided_keys = params.keys()
            for key in provided_keys:
                assert key in valid_keys, f"Can't update parameters for model '{self.abbr}' using unknown key '{key}'."
                self.params[key] = params[key]

    def __eq__(self, other):
        cond1 = self.abbr == other.abbr
        cond2 = set(self.params) == set(other.params)
        cond3 = False not in {self.params[k] == other.params[k] for k in self.params.keys()}
        return cond1 and cond2 and cond3

    def asdict(self) -> dict:
        return {
            "abbr": self.abbr,
            "params": self.params,
        }
