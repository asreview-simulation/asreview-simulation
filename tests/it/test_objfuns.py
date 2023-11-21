import os
import shutil
import sqlite3
from typing import Dict
from typing import Tuple
from typing import Optional
from pathlib import Path
from tempfile import TemporaryDirectory
from asreviewcontrib.insights.metrics import recall as calc_recall
from asreviewcontrib.insights.metrics import wss as calc_wss
from asreview import open_state
import pytest


def get_rows(with_priors=False):
    values = ["pex"] * 3 + ["pin"] * 2 + ["in", "ex", "in", "ex", "in"] + ["ex"] * 15
    return values[:-5] if with_priors else values


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
        "ex": (0, None)
    }
    records = [mapper[k] for k in rows]

    # push the data to the database
    con = sqlite3.connect(d / "results.sql")
    cur = con.cursor()
    cur.execute("CREATE TABLE results(record_id INTEGER, label INTEGER, classifier TEXT, query_strategy TEXT, balance_strategy TEXT, feature_extraction TEXT, training_set INTEGER, labeling_time INTEGER, notes TEXT)")
    cur.execute("CREATE TABLE record_table(record_id INTEGER)")
    cur.execute("CREATE TABLE last_probabilities(proba REAL)")
    cur.execute("CREATE TABLE last_ranking(record_id INTEGER)")
    cur.execute("CREATE TABLE decision_changes(record_id INTEGER)")
    for record in records:
        cur.execute("INSERT into results(label, query_strategy) VALUES(?, ?)", record)
    con.commit()
    con.close()

    # fabricate additional files
    with open(p_tmp / "project.json", "wt") as fid:
        fid.write("""
{
  "id": "",
  "reviews": [
    {
      "id": "123"
    }
  ]
}""")
    with open(d / "settings_metadata.json", "wt") as fid:
        fid.write("""
{
  "settings": null,
  "state_version": "1",
  "software_version": null,
  "model_has_trained": null
}""")

    # zip the project directory, remove the zip file extension
    shutil.make_archive(os.sep.join(p.parts), "zip", p_tmp)
    os.rename(f"{os.sep.join(p.parts)}.zip", os.sep.join(p.parts))
    return p


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 0),
    ("5%", 1),
    ("10%", 1),
    ("15%", 2),
    ("20%", 2),
    ("25%", 3),
    ("30%", 3),
    ("35%", 3),
    ("40%", 3),
    ("45%", 3),
    ("50%", 3),
    ("55%", 3),
    ("60%", 3),
    ("65%", 3),
    ("70%", 3),
    ("75%", 3),
    ("80%", 3),
    ("85%", 3),
    ("90%", 3),
    ("95%", 3),
    ("100%", 3),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_recall_exclude_priors_absolute(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": True,
                "priors": False,
            }
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == expected


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 0 / 3),
    ("5%", 1 / 3),
    ("10%", 1 / 3),
    ("15%", 2 / 3),
    ("20%", 2 / 3),
    ("25%", 3 / 3),
    ("30%", 3 / 3),
    ("35%", 3 / 3),
    ("40%", 3 / 3),
    ("45%", 3 / 3),
    ("50%", 3 / 3),
    ("55%", 3 / 3),
    ("60%", 3 / 3),
    ("65%", 3 / 3),
    ("70%", 3 / 3),
    ("75%", 3 / 3),
    ("80%", 3 / 3),
    ("85%", 3 / 3),
    ("90%", 3 / 3),
    ("95%", 3 / 3),
    ("100%", 3 / 3),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_recall_exclude_priors_relative(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": False,
                "priors": False,
            }
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == pytest.approx(expected)


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 0),
    ("5%", 0),
    ("10%", 0),
    ("15%", 0),
    ("20%", 1),
    ("25%", 2),
    ("30%", 3),
    ("35%", 3),
    ("40%", 4),
    ("45%", 4),
    ("50%", 5),
    ("55%", 5),
    ("60%", 5),
    ("65%", 5),
    ("70%", 5),
    ("75%", 5),
    ("80%", 5),
    ("85%", 5),
    ("90%", 5),
    ("95%", 5),
    ("100%", 5),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_recall_include_priors_absolute(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows(with_priors=True))
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": True,
                "priors": True,
            }
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == expected


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 0 / 5),
    ("5%", 0 / 5),
    ("10%", 0 / 5),
    ("15%", 0 / 5),
    ("20%", 1 / 5),
    ("25%", 2 / 5),
    ("30%", 3 / 5),
    ("35%", 3 / 5),
    ("40%", 4 / 5),
    ("45%", 4 / 5),
    ("50%", 5 / 5),
    ("55%", 5 / 5),
    ("60%", 5 / 5),
    ("65%", 5 / 5),
    ("70%", 5 / 5),
    ("75%", 5 / 5),
    ("80%", 5 / 5),
    ("85%", 5 / 5),
    ("90%", 5 / 5),
    ("95%", 5 / 5),
    ("100%", 5 / 5),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_recall_include_priors_relative(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows(with_priors=True))
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": False,
                "priors": True,
            }
            actual = calc_recall(s, int(at_pct[:-1]) / 100, **kwargs)
            assert actual == pytest.approx(expected)


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 12),
    ("5%", 12),
    ("10%", 12),
    ("15%", 12),
    ("20%", 12),
    ("25%", 12),
    ("30%", 12),
    ("35%", 4),
    ("40%", 4),
    ("45%", 4),
    ("50%", 4),
    ("55%", 4),
    ("60%", 4),
    ("65%", 4),
    ("70%", 8),
    ("75%", 8),
    ("80%", 8),
    ("85%", 8),
    ("90%", 8),
    ("95%", 8),
    ("100%", 12),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_wss_exclude_priors_absolute(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows())
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": True,
                "priors": False,
            }
            actual = calc_wss(s, int(at_pct[:-1]) / 100, **kwargs)
            pytest.xfail("TODO these values aren't right")
            assert actual == expected


@pytest.mark.parametrize("at_pct, expected", [
    ("0%", 1/5 + 1/3),
    ("5%", 1/5 + 1/3),
    ("10%", 1/5 + 1/3),
    ("15%", 1/5 + 1/3),
    ("20%", 1/5 + 1/3),
    ("25%", 1/5 + 1/3),
    ("30%", 1/5 + 1/3),
    ("35%", 1/5),
    ("40%", 1/5),
    ("45%", 1/5),
    ("50%", 1/5),
    ("55%", 1/5),
    ("60%", 1/5),
    ("65%", 1/5),
    ("70%", 1/3),
    ("75%", 1/3),
    ("80%", 1/3),
    ("85%", 1/3),
    ("90%", 1/3),
    ("95%", 1/3),
    ("100%", 1/5 + 1/3),
    ], ids=[f"{pct}%" for pct in range(0, 101, 5)])
def test_wss_exclude_priors_relative(at_pct, expected):
    with TemporaryDirectory(prefix="tmp.ofn-testing.", dir=".") as tmpdir:
        p = make_fixtures(tmpdir, get_rows(with_priors=True))
        with open_state(os.sep.join(p.parts)) as s:
            kwargs = {
                "x_absolute": False,
                "y_absolute": False,
                "priors": False,
            }
            actual = calc_wss(s, int(at_pct[:-1]) / 100, **kwargs)
            pytest.fail("TODO these values aren't right")
            assert actual == pytest.approx(expected)
