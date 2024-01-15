import re
from pathlib import Path
import pytest
import tomli
import yaml


@pytest.fixture
def expected_version(project_root):
    fname = project_root / "pyproject.toml"
    with open(fname, "rb") as f:
        toml_dict = tomli.load(f)
    return toml_dict["project"]["version"]


@pytest.fixture
def project_root():
    return Path(__file__).parent.parent.parent


def test_version_citation_cff(expected_version, project_root):
    fname = project_root / "CITATION.cff"
    with open(fname, "rb") as f:
        yaml_dict = yaml.safe_load(f)
    actual_version = yaml_dict["version"]
    assert actual_version == expected_version


def test_version_readme_md_badge_repo(expected_version, project_root):
    fname = project_root / "README.md"
    with open(fname, "rt") as f:
        txt = f.read()
    rexp = r"^.*GitHub release \(with filter\).*/tree/(?P<version>[^\)]+).*$"
    actual_version = re.search(rexp, txt, re.MULTILINE).group("version")
    assert actual_version == expected_version


def test_version_readme_md_badge_commits(expected_version, project_root):
    fname = project_root / "README.md"
    with open(fname, "rt") as f:
        txt = f.read()
    rexp = (
        r"^.*GitHub commits since latest release.*/commits-since/asre"
        + r"view-simulation/asreview-simulation/(?P<version>[^\)]+).*$"
    )
    actual_version = re.search(rexp, txt, re.MULTILINE).group("version")
    assert actual_version == expected_version


def test_version_readme_md_badge_commits_compare(expected_version, project_root):
    fname = project_root / "README.md"
    with open(fname, "rt") as f:
        txt = f.read()
    rexp = r"^.*GitHub commits since latest release.*/compare/(?P<version>\d\.\d\.\d.*)\.{3}HEAD.*$"
    actual_version = re.search(rexp, txt, re.MULTILINE).group("version")
    assert actual_version == expected_version


def test_version_readme_md_install(expected_version, project_root):
    fname = project_root / "README.md"
    with open(fname, "rt") as f:
        txt = f.read()
    rexp = r"^pip install git\+https://github\.com/asreview-simulation/asreview-simulation\.git@(?P<version>.*)$"
    actual_version = re.search(rexp, txt, re.MULTILINE).group("version")
    assert actual_version == expected_version


def test_version_readme_md_install_with_optionals(expected_version, project_root):
    fname = project_root / "README.md"
    with open(fname, "rt") as f:
        txt = f.read()
    rexp = (
        r"^pip install asreview-simulation\[doc2vec\]@git\+https://gith"
        + r"ub\.com/asreview-simulation/asreview-simulation\.git@(?P<version>.*)$"
    )
    actual_version = re.search(rexp, txt, re.MULTILINE).group("version")
    assert actual_version == expected_version
