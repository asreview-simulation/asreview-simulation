from typing import Callable
from typing import cast
from typing import List
from typing import Optional
from typing import Tuple
from asreview.data import ASReviewData
from asreviewcontrib.simulation._private.lib.config import Config
from asreviewcontrib.simulation._private.lib.get_quads import get_quads
from asreviewcontrib.simulation._private.lib.sam.sam_handpicked_unwrap import sam_handpicked_unwrap
from asreviewcontrib.simulation._private.lib.sam.sam_random_unwrap import sam_random_unwrap


TSamResult = Tuple[List[int], int, int, Optional[int]]
TFunc = Callable[[Config, ASReviewData], TSamResult]


def unwrap_prior_sampling_vars(config: Config, as_data: ASReviewData) -> TSamResult:
    my_sams = {
        "sam-handpicked": sam_handpicked_unwrap,
        "sam-random": sam_random_unwrap,
    }

    other_sams = [{abbr: q.impl} for abbr, q in get_quads()]

    sams = my_sams
    for other_sam in other_sams:
        sams.update(other_sam)

    try:
        func: TFunc = cast(TFunc, sams[config.sam.abbr])
    except KeyError as e:
        abbrs = "\n".join(list(sams.keys()))
        print(f"'{config.sam.abbr}' is not a valid name for a sam model. Valid names are:\n{abbrs}")
        raise e

    return func(config, as_data)
