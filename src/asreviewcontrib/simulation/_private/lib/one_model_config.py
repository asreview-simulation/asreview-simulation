from typing import Dict
from typing import Optional
from asreviewcontrib.simulation._private.lib.get_default_params import get_default_params


class OneModelConfig:
    def __init__(self, abbr: str, params: Optional[Dict] = None):
        assert isinstance(abbr, str), "Expected input argument 'abbr' to be of type 'str'"
        default_params = get_default_params(abbr)
        self._abbr = abbr
        self._params = default_params
        if params is not None:
            assert isinstance(params, dict), "Expected input argument 'params' to be of type 'dict'"
            valid_keys = default_params.keys()
            provided_keys = params.keys()
            for key in provided_keys:
                assert key in valid_keys, f"Can't update parameters for model '{self._abbr}' using unknown key '{key}'."
                self._params[key] = params[key]

    def __eq__(self, other):
        cond1 = self._abbr == other._abbr
        cond2 = set(self._params) == set(other._params)
        cond3 = False not in {self._params[k] == other._params[k] for k in self._params.keys()}
        return cond1 and cond2 and cond3

    def as_dict(self) -> dict:
        return {
            "abbr": self._abbr,
            "params": self._params,
        }

    def flattened(self):
        d = {}
        for param in self.params.keys():
            k = "/".join([self.abbr, param])
            v = self.params[param]
            d.update({k: v})
        return d

    @property
    def abbr(self):
        return self._abbr

    @property
    def params(self):
        return self._params
