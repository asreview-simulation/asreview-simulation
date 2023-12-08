from asreviewcontrib.simulation._private.lib.config import Config


class Provided:
    _errmsg = "Expected a bool"

    def __init__(self):
        self._bal = False
        self._clr = False
        self._fex = False
        self._ofn = False
        self._qry = False
        self._sam = False
        self._stp = False

    @property
    def bal(self) -> bool:
        return self._bal

    @bal.setter
    def bal(self, bal: bool):
        assert isinstance(bal, bool), Provided._errmsg
        self._bal = bal

    @property
    def clr(self) -> bool:
        return self._clr

    @clr.setter
    def clr(self, clr: bool):
        assert isinstance(clr, bool), Provided._errmsg
        self._clr = clr

    @property
    def fex(self) -> bool:
        return self._fex

    @fex.setter
    def fex(self, fex: bool):
        assert isinstance(fex, bool), Provided._errmsg
        self._fex = fex

    @property
    def ofn(self) -> bool:
        return self._ofn

    @ofn.setter
    def ofn(self, ofn: bool):
        assert isinstance(ofn, bool), Provided._errmsg
        self._ofn = ofn

    @property
    def qry(self) -> bool:
        return self._qry

    @qry.setter
    def qry(self, qry: bool):
        assert isinstance(qry, bool), Provided._errmsg
        self._qry = qry

    @property
    def sam(self) -> bool:
        return self._sam

    @sam.setter
    def sam(self, sam: bool):
        assert isinstance(sam, bool), Provided._errmsg
        self._sam = sam

    @property
    def stp(self) -> bool:
        return self._stp

    @stp.setter
    def stp(self, stp: bool):
        assert isinstance(stp, bool), Provided._errmsg
        self._stp = stp


class State:
    def __init__(self):
        self.config = Config()
        self.provided = Provided()
