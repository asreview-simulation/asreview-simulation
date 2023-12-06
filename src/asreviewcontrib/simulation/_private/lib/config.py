from typing import Dict
from typing import Optional
from asreviewcontrib.simulation._private.lib.get_default_params import get_default_params


class OneModelConfig:
    """Stores the configuration for one model, e.g. the balancer, the stopping model,
    or the objective function model."""
    def __init__(self, abbr: str, params: Optional[Dict] = None):
        """Constructor method. Some example usages:

        1. Default parameter values given the choice for `bal-simple`.
            ```python
            from asreviewcontrib.simulation.api import OneModelConfig


            bal = OneModelConfig(abbr="bal-simple")
            ```
        2. Custom parameter values for the selected model choice `stp-nq`.
            ```python
            from asreviewcontrib.simulation.api import OneModelConfig


            stp = OneModelConfig(abbr="stp-nq", params={"n_queries: 20"})
            ```
        3. Partially custom parameter values for the selected model choice `qry-max-random`.
            ```python
            from asreviewcontrib.simulation.api import OneModelConfig


            qry = OneModelConfig(abbr="qry-max-random", params={"n_instances: 10"})
            ```
        """
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
        """Test whether this instance of `OneModelConfig` is exactly equal to the `other` instance
        with respect to the set of key names and their values."""
        cond1 = self._abbr == other._abbr
        cond2 = set(self._params) == set(other._params)
        cond3 = False not in {self._params[k] == other._params[k] for k in self._params.keys()}
        return cond1 and cond2 and cond3

    def as_dict(self) -> dict:
        """Returns the model configuration as a `dict`."""
        return {
            "abbr": self._abbr,
            "params": self._params,
        }

    def flattened(self):
        """Returns a flattened version of the model configuration as a `dict` whose keys consist
        of the name of the model and the name of its parameters."""
        d = {}
        for param in self.params.keys():
            k = "/".join([self.abbr, param])
            v = self.params[param]
            d.update({k: v})
        return d

    @property
    def abbr(self) -> str:
        """Read-only property that returns the model abbreviation."""
        return self._abbr

    @property
    def params(self) -> dict:
        """Read-only property that returns the model parameterization."""
        return self._params


class Config:
    _errmsg = "Expected an instance of OneModelConfig"

    def __init__(
        self,
        bal: Optional[OneModelConfig] = None,
        cls: Optional[OneModelConfig] = None,
        fex: Optional[OneModelConfig] = None,
        ofn: Optional[OneModelConfig] = None,
        qry: Optional[OneModelConfig] = None,
        sam: Optional[OneModelConfig] = None,
        stp: Optional[OneModelConfig] = None,
    ):
        """Constructor method. Some example usages:

        1. Default choice for each model type, default configuration for each model.
            ```python
            from asreviewcontrib.simulation.api import Config


            config = Config()
            ```
        2. Default choice for each model type except balancer, default
        parameter values for all models.
            ```python
            from asreviewcontrib.simulation.api import Config
            from asreviewcontrib.simulation.api import OneModelConfig


            bal = OneModelConfig(abbr="bal-simple")
            config = Config(bal=bal)
            ```
        3. Custom model choice for sampling model and for stopping model,
        other model types use their default choice and parameterization.
            ```python
            from asreviewcontrib.simulation.api import Config
            from asreviewcontrib.simulation.api import OneModelConfig


            custom = {
                "sam": OneModelConfig(abbr="sam-random", params={
                    "n_excluded": 10,
                    "n_included": 10,
                }),
                "stp": OneModelConfig(abbr="stp-nq"),
            config = Config(*custom)
            ```
        """

        # initialize the private attributes:
        self._bal = None
        self._cls = None
        self._fex = None
        self._ofn = None
        self._qry = None
        self._sam = None
        self._stp = None

        # use the setter methods to assign constructor arguments to private attributes
        self.bal = bal or OneModelConfig("bal-double")
        self.cls = cls or OneModelConfig("cls-nb")
        self.fex = fex or OneModelConfig("fex-tfidf")
        self.ofn = ofn or OneModelConfig("ofn-none")
        self.qry = qry or OneModelConfig("qry-max")
        self.sam = sam or OneModelConfig("sam-random")
        self.stp = stp or OneModelConfig("stp-rel")

    def __eq__(self, other):
        return False not in {
            self._bal == other._bal,
            self._cls == other._cls,
            self._fex == other._fex,
            self._ofn == other._ofn,
            self._qry == other._qry,
            self._sam == other._sam,
            self._stp == other._stp,
        }

    def as_dict(self, recurse=True) -> dict:
        return {
            "bal": self._bal.as_dict() if recurse else self._bal,
            "cls": self._cls.as_dict() if recurse else self._cls,
            "fex": self._fex.as_dict() if recurse else self._fex,
            "ofn": self._ofn.as_dict() if recurse else self._ofn,
            "qry": self._qry.as_dict() if recurse else self._qry,
            "sam": self._sam.as_dict() if recurse else self._stp,
            "stp": self._stp.as_dict() if recurse else self._sam,
        }

    def flattened(self) -> dict:
        d = {}
        d.update(self.bal.flattened())
        d.update(self.cls.flattened())
        d.update(self.fex.flattened())
        d.update(self.ofn.flattened())
        d.update(self.qry.flattened())
        d.update(self.sam.flattened())
        d.update(self.stp.flattened())
        return d

    @property
    def bal(self) -> OneModelConfig:
        """Returns the configuration for the balancer model."""
        return self._bal

    @bal.setter
    def bal(self, bal: OneModelConfig):
        assert isinstance(bal, OneModelConfig), Config._errmsg
        assert bal.abbr.startswith("bal"), "Expected a balancer model."
        self._bal = bal

    @property
    def cls(self) -> OneModelConfig:
        """Returns the configuration for the classifier model."""
        return self._cls

    @cls.setter
    def cls(self, cls: OneModelConfig):
        assert isinstance(cls, OneModelConfig), Config._errmsg
        assert cls.abbr.startswith("cls"), "Expected a classifier model."
        self._cls = cls

    @property
    def fex(self) -> OneModelConfig:
        """Returns the configuration for the feature extraction model."""
        return self._fex

    @fex.setter
    def fex(self, fex: OneModelConfig):
        assert isinstance(fex, OneModelConfig), Config._errmsg
        assert fex.abbr.startswith("fex"), "Expected a feature extraction model."
        self._fex = fex

    @property
    def ofn(self) -> OneModelConfig:
        """Returns the configuration for the objective function model."""
        return self._ofn

    @ofn.setter
    def ofn(self, ofn: OneModelConfig):
        assert isinstance(ofn, OneModelConfig), Config._errmsg
        assert ofn.abbr.startswith("ofn"), "Expected an objective function model."
        self._ofn = ofn

    @property
    def qry(self) -> OneModelConfig:
        """Returns the configuration for the query model."""
        return self._qry

    @qry.setter
    def qry(self, qry: OneModelConfig):
        assert isinstance(qry, OneModelConfig), Config._errmsg
        assert qry.abbr.startswith("qry"), "Expected a query model."
        self._qry = qry

    @property
    def sam(self) -> OneModelConfig:
        """Returns the configuration for the sampling model."""
        return self._sam

    @sam.setter
    def sam(self, sam: OneModelConfig):
        assert isinstance(sam, OneModelConfig), Config._errmsg
        assert sam.abbr.startswith("sam"), "Expected a sampler model."
        self._sam = sam

    @property
    def stp(self) -> OneModelConfig:
        """Returns the configuration for the stopping model."""
        return self._stp

    @stp.setter
    def stp(self, stp: OneModelConfig):
        assert isinstance(stp, OneModelConfig), Config._errmsg
        assert stp.abbr.startswith("stp"), "Expected a stopping model."
        self._stp = stp