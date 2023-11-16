from typing import Optional
from asreview_simulation._private.lib.get_default_params import get_default_params


class PartialConfig:
    def __init__(self, abbr: str, params: Optional[dict] = None):
        assert type(abbr) == str, "Expected input argument 'abbr' to be of type 'str'"
        default_params = get_default_params(abbr)
        self.abbr = abbr
        self.params = default_params
        if params is not None:
            assert type(params) == dict, "Expected input argument 'params' to be of type 'dict'"
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


class CompleteConfig:
    def __init__(
        self,
        bal: PartialConfig = None,
        cls: PartialConfig = None,
        fex: PartialConfig = None,
        qry: PartialConfig = None,
        sam: PartialConfig = None,
        stp: PartialConfig = None,
    ):
        self.bal = bal or PartialConfig("bal-double")
        self.cls = cls or PartialConfig("cls-nb")
        self.fex = fex or PartialConfig("fex-tfidf")
        self.qry = qry or PartialConfig("qry-max")
        self.sam = sam or PartialConfig("sam-random")
        self.stp = stp or PartialConfig("stp-rel")

        assert self.bal.abbr.startswith("bal"), "Expected input argument 'bal' to contain a balancer model."
        assert self.cls.abbr.startswith("cls"), "Expected input argument 'cls' to contain a classifier model."
        assert self.fex.abbr.startswith("fex"), "Expected input argument 'fex' to contain a feature extraction model."
        assert self.qry.abbr.startswith("qry"), "Expected input argument 'qry' to contain a query model."
        assert self.sam.abbr.startswith("sam"), "Expected input argument 'sam' to contain a prior sampling model."
        assert self.stp.abbr.startswith("stp"), "Expected input argument 'stp' to contain a stopping model."

    def __eq__(self, other):
        return False not in {
            self.bal == other.bal,
            self.cls == other.cls,
            self.fex == other.fex,
            self.qry == other.qry,
            self.sam == other.sam,
            self.stp == other.stp,
        }

    def asdict(self) -> dict:
        return {
            "bal": self.bal.asdict(),
            "cls": self.cls.asdict(),
            "fex": self.fex.asdict(),
            "qry": self.qry.asdict(),
            "sam": self.sam.asdict(),
            "stp": self.stp.asdict(),
        }
