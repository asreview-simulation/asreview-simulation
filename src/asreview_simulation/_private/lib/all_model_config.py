from typing import Optional
from asreview_simulation._private.lib.one_model_config import OneModelConfig


class AllModelConfig:
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

    @property
    def bal(self) -> OneModelConfig:
        return self._bal

    @bal.setter
    def bal(self, bal: OneModelConfig):
        assert isinstance(bal, OneModelConfig), AllModelConfig._errmsg
        assert bal.abbr.startswith("bal"), "Expected a balancer model."
        self._bal = bal

    @property
    def cls(self) -> OneModelConfig:
        return self._cls

    @cls.setter
    def cls(self, cls: OneModelConfig):
        assert isinstance(cls, OneModelConfig), AllModelConfig._errmsg
        assert cls.abbr.startswith("cls"), "Expected a classifier model."
        self._cls = cls

    @property
    def fex(self) -> OneModelConfig:
        return self._fex

    @fex.setter
    def fex(self, fex: OneModelConfig):
        assert isinstance(fex, OneModelConfig), AllModelConfig._errmsg
        assert fex.abbr.startswith("fex"), "Expected a feature extraction model."
        self._fex = fex

    @property
    def ofn(self) -> OneModelConfig:
        return self._ofn

    @ofn.setter
    def ofn(self, ofn: OneModelConfig):
        assert isinstance(ofn, OneModelConfig), AllModelConfig._errmsg
        assert ofn.abbr.startswith("ofn"), "Expected an objective function model."
        self._ofn = ofn

    @property
    def qry(self) -> OneModelConfig:
        return self._qry

    @qry.setter
    def qry(self, qry: OneModelConfig):
        assert isinstance(qry, OneModelConfig), AllModelConfig._errmsg
        assert qry.abbr.startswith("qry"), "Expected a query model."
        self._qry = qry

    @property
    def sam(self) -> OneModelConfig:
        return self._sam

    @sam.setter
    def sam(self, sam: OneModelConfig):
        assert isinstance(sam, OneModelConfig), AllModelConfig._errmsg
        assert sam.abbr.startswith("sam"), "Expected a sampler model."
        self._sam = sam

    @property
    def stp(self) -> OneModelConfig:
        return self._stp

    @stp.setter
    def stp(self, stp: OneModelConfig):
        assert isinstance(stp, OneModelConfig), AllModelConfig._errmsg
        assert stp.abbr.startswith("stp"), "Expected a stopping model."
        self._stp = stp
