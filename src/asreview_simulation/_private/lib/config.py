from asreview_simulation._private.lib.get_default_config import get_default_config


class PartialConfig:
    def __init__(self, abbr: str, params: dict):
        self.abbr = abbr
        self.params = params

    def asdict(self):
        return {
            "abbr": self.abbr,
            "params": self.params,
        }


class CompleteConfig:
    def __init__(self, bal=None, cls=None, fex=None, qry=None, sam=None, stp=None):
        self.bal = bal or get_default_config("bal-double")
        self.cls = cls or get_default_config("cls-nb")
        self.fex = fex or get_default_config("fex-tfidf")
        self.qry = qry or get_default_config("qry-max")
        self.sam = sam or get_default_config("sam-random")
        self.stp = stp or get_default_config("stp-rel")

    def asdict(self):
        return {
            "bal": self.bal.asdict(),
            "cls": self.cls.asdict(),
            "fex": self.fex.asdict(),
            "qry": self.qry.asdict(),
            "sam": self.sam.asdict(),
            "stp": self.stp.asdict(),
        }
