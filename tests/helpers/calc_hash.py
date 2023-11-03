import hashlib


def calc_hash(filename):
    with open(filename, "rb") as f:
        contents = f.read()
        return hashlib.sha256(contents).hexdigest()
