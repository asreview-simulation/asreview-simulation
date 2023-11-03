import os
import zipfile
from pathlib import Path


def unzip_simulate_results(p):
    src = p.parent / Path(p.name + ".tmp")
    tgt = p
    os.rename(tgt, src)
    with zipfile.ZipFile(src, "r") as f:
        f.extractall(tgt)
    os.remove(src)
