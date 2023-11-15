from asreview_simulation._private.lib.get_default_params import get_default_params


class PartialConfig:
    def __init__(self, abbr: str, params: dict | None = None):
        default_params = get_default_params(abbr)
        self.abbr = abbr
        self.params = default_params
        if params is not None:
            valid_keys = default_params.keys()
            provided_keys = params.keys()
            for key in provided_keys:
                assert key in valid_keys, f"Can't update parameters for model '{self.abbr}' using unknown key '{key}'."
                self.params[key] = params[key]

    def asdict(self) -> dict:
        return {
            "abbr": self.abbr,
            "params": self.params,
        }


class CompleteConfig:
    def __init__(self, bal: PartialConfig = None, cls: PartialConfig = None, fex: PartialConfig = None, qry: PartialConfig = None, sam: PartialConfig = None, stp: PartialConfig = None):
        self.bal = bal or PartialConfig("bal-double")
        self.cls = cls or PartialConfig("cls-nb")
        self.fex = fex or PartialConfig("fex-tfidf")
        self.qry = qry or PartialConfig("qry-max")
        self.sam = sam or PartialConfig("sam-random")
        self.stp = stp or PartialConfig("stp-rel")

    def asdict(self) -> dict:
        return {
            "bal": self.bal.asdict(),
            "cls": self.cls.asdict(),
            "fex": self.fex.asdict(),
            "qry": self.qry.asdict(),
            "sam": self.sam.asdict(),
            "stp": self.stp.asdict(),
        }
