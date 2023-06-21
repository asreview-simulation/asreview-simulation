from ._calc_hash import calc_hash
from pathlib import Path


def compare_data_csv(p1, p2, data=None, dataset=None):
    if dataset is not None:
        if dataset.startswith("benchmark:"):
            fname = f"{dataset[10:]}.csv"
        else:
            fname = f"{dataset}.csv"
    elif data is not None:
        fname = Path(data).with_suffix(".csv").name
    else:
        raise ValueError("Unexpectedly did not receive a value for 'data' nor for 'dataset'.")

    assert calc_hash(p1 / "data" / fname) == calc_hash(p2 / "data" / fname)
