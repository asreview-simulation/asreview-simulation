import os
from pathlib import Path


def rename_simulation_results(p):
    src = p.parent / Path(p.name + ".tmp")
    tgt = p
    os.rename(src, tgt)
