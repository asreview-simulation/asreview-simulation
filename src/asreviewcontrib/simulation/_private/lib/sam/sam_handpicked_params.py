from typing import List
from typing import Optional
from typing import TypedDict


class ParamsType(TypedDict):
    records: Optional[List[int]]
    rows: Optional[List[int]]


def get_sam_handpicked_params() -> ParamsType:
    return {
        "records": None,
        "rows": None,
    }
