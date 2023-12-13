from typing import Literal
from typing import Union
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config
from asreviewcontrib.simulation._private.lib.stp.stp_none_unwrap import stp_none_unwrap
from asreviewcontrib.simulation._private.lib.stp.stp_nq_unwrap import stp_nq_unwrap
from asreviewcontrib.simulation._private.lib.stp.stp_rel_unwrap import stp_rel_unwrap
from asreviewcontrib.simulation._private.lib.get_quads import get_quads


def unwrap_stopping_vars(config: Config, as_data: ASReviewData) -> Union[int, Literal["min"]]:

    my_stps = {
        "stp-none": stp_none_unwrap,
        "stp-nq": stp_nq_unwrap,
        "stp-rel": stp_rel_unwrap,
    }

    other_stps = [{abbr: q.impl} for abbr, q in get_quads()]

    stps = my_stps
    for other_stp in other_stps:
        stps.update(other_stp)

    try:
        return stps[config.stp.abbr](config, as_data)
    except KeyError as e:
        abbrs = "\n".join(list(stps.keys()))
        print(f"'{config.stp.abbr}' is not a valid name for an stp model. Valid names are:\n{abbrs}")
        raise e
