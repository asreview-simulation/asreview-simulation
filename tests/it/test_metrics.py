import os
import shutil
import sqlite3
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Dict
from typing import Optional
from typing import Tuple
import pytest
from asreview import open_state
from asreviewcontrib.insights.metrics import recall as calc_recall
from asreviewcontrib.insights.metrics import wss as calc_wss


def get_rows():
    values = ["pex"] * 1 + ["pin"] * 1 + ["in", "in", "in", "ex", "in", "ex", "in", "ex", "ex", "ex"]
    return values


def get_kwargs(absolute=False, priors=False):
    return {
        "x_absolute": False,
        "y_absolute": absolute,
        "priors": priors,
    }


def make_fixtures(tmpdir, rows):
    # prepare the asreview project tmp directory
    project_id = "123"
    p = Path(tmpdir) / "project.asreview"
    p_tmp = Path(tmpdir) / "project.asreview.tmp"
    d = p_tmp / "reviews" / project_id
    os.makedirs(d)

    # prepare the data
    mapper: Dict[str, Tuple[int, Optional[str]]] = {
        "pin": (1, "prior"),
        "pex": (0, "prior"),
        "in": (1, None),
        "ex": (0, None),
    }
    records = [mapper[k] for k in rows]

    # push the data to the database
    con = sqlite3.connect(d / "results.sql")
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE results(record_id INTEGER, label INTEGER, classifier TEXT, query_strate"
        + "gy TEXT, balance_strategy TEXT, feature_extraction TEXT, training_set INTEGER, label"
        + "ing_time INTEGER, notes TEXT)"
    )
    cur.execute("CREATE TABLE record_table(record_id INTEGER)")
    cur.execute("CREATE TABLE last_probabilities(proba REAL)")
    cur.execute("CREATE TABLE last_ranking(record_id INTEGER)")
    cur.execute("CREATE TABLE decision_changes(record_id INTEGER)")
    for record in records:
        cur.execute("INSERT into results(label, query_strategy) VALUES(?, ?)", record)
        cur.execute("INSERT into record_table(record_id) VALUES(?)", (None,))
    con.commit()
    con.close()

    # fabricate additional files
    with open(p_tmp / "project.json", "wt") as fid:
        fid.write(
            """
{
  "id": "",
  "reviews": [
    {
      "id": "123"
    }
  ]
}"""
        )
    with open(d / "settings_metadata.json", "wt") as fid:
        fid.write(
            """
{
  "settings": null,
  "state_version": "1",
  "software_version": null,
  "model_has_trained": null
}"""
        )

    # zip the project directory, remove the zip file extension
    shutil.make_archive(os.sep.join(p.parts), "zip", p_tmp)
    os.rename(f"{os.sep.join(p.parts)}.zip", os.sep.join(p.parts))
    return p


@pytest.mark.parametrize(
    "at_pct, expected",
    [
        ("0%", 0),
        ("20%", 2),
        ("40%", 3),
        ("60%", 4),
        ("80%", 5),
        ("100%", 5),
    ],
    ids=[f"{pct}%" for pct in range(0, 101, 20)],
)
def test_recall_absolute(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        kwargs = get_kwargs(absolute=True)
        with open_state(os.sep.join(p.parts)) as s:
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == expected


@pytest.mark.parametrize(
    "at_pct, expected",
    [
        ("0%", 0 / 5),
        ("20%", 2 / 5),
        ("40%", 3 / 5),
        ("60%", 4 / 5),
        ("80%", 5 / 5),
        ("100%", 5 / 5),
    ],
    ids=[f"{pct}%" for pct in range(0, 101, 20)],
)
def test_recall_relative(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = get_kwargs()
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == pytest.approx(expected)


# @pytest.mark.skip("test passes but expected numbers may be wrong?")
@pytest.mark.parametrize(
    "at_pct, expected",
    [
        ("0%", 0),
        ("20%", 1),
        ("40%", 2),
        ("60%", 3),
        ("80%", 3),
        ("100%", 3),
    ],
    ids=[f"{pct}%" for pct in range(0, 101, 20)],
)
def test_wss_absolute(at_pct, expected):
    if at_pct in {"0%"}:
        pytest.xfail(reason="interpolation problem in 'asreview-insights' package")
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = get_kwargs(absolute=True)
            actual = calc_wss(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == expected


# @pytest.mark.skip("test passes but expected numbers may be wrong?")
@pytest.mark.parametrize(
    "at_pct, expected",
    [
        ("0%", 0 / 10),
        ("20%", 1 / 10),
        ("40%", 2 / 10),
        ("60%", 3 / 10),
        ("80%", 3 / 10),
        ("100%", 3 / 10),
    ],
    ids=[f"{pct}%" for pct in range(0, 101, 20)],
)
def test_wss_relative(at_pct, expected):
    if at_pct in {"0%"}:
        pytest.xfail(reason="interpolation problem in 'asreview-insights' package")
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = get_kwargs()
            actual = calc_wss(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == pytest.approx(expected)
