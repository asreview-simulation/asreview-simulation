from asreview_simulation._private.lib.one_model_config import OneModelConfig


class AllModelConfig:
    def __init__(
        self,
        bal: OneModelConfig = None,
        cls: OneModelConfig = None,
        fex: OneModelConfig = None,
        qry: OneModelConfig = None,
        sam: OneModelConfig = None,
        stp: OneModelConfig = None,
    ):
        self.bal = bal or OneModelConfig("bal-double")
        self.cls = cls or OneModelConfig("cls-nb")
        self.fex = fex or OneModelConfig("fex-tfidf")
        self.qry = qry or OneModelConfig("qry-max")
        self.sam = sam or OneModelConfig("sam-random")
        self.stp = stp or OneModelConfig("stp-rel")

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
