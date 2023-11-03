from pathlib import Path
from tests.helpers.calc_hash import calc_hash


def compare_data_csv(p1, p2, benchmark=None, input_file=None):
    if benchmark is not None:
        if benchmark.startswith("benchmark:"):
            fname = f"{benchmark[10:]}.csv"
        else:
            fname = f"{benchmark}.csv"
    elif input_file is not None:
        fname = Path(input_file).with_suffix(".csv").name
    else:
        raise ValueError("Unexpectedly did not receive a value for 'input_file' nor for 'benchmark'.")

    assert calc_hash(p1 / "data" / fname) == calc_hash(p2 / "data" / fname)
