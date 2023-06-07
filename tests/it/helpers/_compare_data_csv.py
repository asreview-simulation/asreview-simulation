from ._calc_hash import calc_hash


def compare_data_csv(p1, p2, dataset):
    fname = (
        f"{dataset[10:]}.csv" if dataset.startswith("benchmark:") else f"{dataset}.csv"
    )
    assert calc_hash(p1 / "data" / fname) == calc_hash(p2 / "data" / fname)
