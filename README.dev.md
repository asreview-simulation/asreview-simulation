# Developer notes

## Install

```shell
mkdir <a directory>
git clone https://github.com/asreview-simulation/asreview-simulation .
python3 -m venv venv
source venv/bin/activate
pip install --editable .
```

There are various sets of dependencies that you should install depending on the work you're planning to do. 

```shell
pip install --editable .[testing]
pip install --editable .[linting]
pip install --editable .[publishing]
pip install --editable .[doc2vec]
pip install --editable .[sbert]
pip install --editable .[tensorflow]
```

You can combine subsets of these into one command like so, e.g.:

```shell
pip install --editable .[linting,testing]
```

## Linting

Running pre-commit on unstaged files

```
pip install --editable .[linting]
pre-commit run --all-files
```

## Testing

There are various types of test: unit tests, tests that use mocking, and integration tests. Each has its own
subdirectory. The tests can be run locally with:

```shell
pip install --editable .[testing]
pytest -v
```

Tests pertaining to a specific model have been marked accordingly with the following markers (see also `pytest`
configuration section in `pyproject.toml` or run `pytest --markers`):

| prior sampling   | feature extractor    | classifier       | querier           | balancer          | stopping   | objective function |
|------------------|----------------------|------------------|-------------------|-------------------|------------|--------------------|
| `sam_handpicked` | `fex_doc2vec`        | `cls_logistic`   | `qry_cluster`     | `bal_double`      | `stp_none` | `ofn_none`         |
| `sam_random`     | `fex_embeding_idf`   | `cls_lstm_base`  | `qry_max`         | `bal_simple`      | `stp_nq`   | `ofn_wss`          |
|                  | `fex_embedding_lstm` | `cls_lstm_pool`  | `qry_max_random`  | `bal_undersample` | `stp_rel`  |                    |
|                  | `fex_sbert`          | `cls_nb`         | `qry_uncertainty` |                   |            |                    |
|                  | `fex_tfidf`          | `cls_nn_2_layer` | `qry_random`      |                   |            |                    |
|                  |                      | `cls_rf`         | `qry_uncertainty` |                   |            |                    |
|                  |                      | `cls_svm`        |                   |                   |            |                    |

You can instruct `pytest` to run only the tests for one or some of these marked sets. As an example, if you want to run
only the tests related to Naive Bayes, you should call `pytest` with the `-m` flag as follows:

```shell
pytest -m cls_nb -v
```

Markers can also be combined with `or` and `and` and `not`, e.g.

```shell
pytest -m 'cls_nb and fex_tfidf' -v
pytest -m 'cls_rf and not fex_embedding_idf and not fex_embedding_lstm' -v
pytest -m 'cls_logistic or cls_rf' -v
# etc
```

Besides running locally, they can also be run on GitHub infrastructure by manually triggering the GitHub Action
workflow `testing`. The workflow tests whether the tests pass for all combinations of operating
system (Windows, Linux, MacOS), asreview version (1.0.4, 1.1.1, 1.2.1), and python version (3.8, 3.9, 3.10, 3.11).

Currently, the `testing` workflow on GitHub skips any tests that require TensorFlow on Python >= 3.11 (tests marked
with `cls_lstm_base`, `cls_lstm_pool`, `cls_nn_2_layer`), because `asreview` has a problem installing TensorFlow on
Python 3.11 and up.

### `tests/unit`

These tests are simple, quick to run, and mostly focus on whether the `asreview-simulation` subcommands manipulate the
state (`obj`) in the correct way. The idea of the "unit" in unit testing is that when the test fails, there is just one
thing that could have gone wrong. This is in contrast to other types of test, e.g. integration testing (see below).

### `tests/api`

These tests help safeguard against accidentally changing the api.

### `tests/use_cases`

These tests are used to automate running some use cases.

### `tests/mocked`

The mocked tests verify whether the arguments that `SimulateReview` receives inside `asreview`'s `SimulateEntrypoint`
are the same arguments as what `SimulateReview` in `asreview_simulate` receives. The simulation inside these tests just
do the setting up of a simulation, including creating some files in a temporary directory, but they do not run. This
makes them faster than the integration tests (see below), but naturally, the simulation does not generate output files,
so there are no results to compare.

### `tests/it`

These are the most extensive type of tests. They set up a simulation using `asreview simulate`, then set up the same
simulation using `asreview simulation [subcommands with options] start`, then compare the resulting files that are
generated inside the `.asreview` file (`project.json`, `data/<dataset>.csv`, `reviews/<id>/results.sql`, and
`reviews/<id>/settings_metadata.json`, but not `feature_matrices/<extractor-method>_feature_matrix.npz` at the moment).

### Static analysis and coverage calculation

The project has been set up to use [SonarCloud](https://sonarcloud.io) to perform static analysis on the code base via
a GitHub Action named `sonarcloud`. The analysis runs on a weekly schedule but can also be triggered manually.
The results can be inspected at SonarCloud: https://sonarcloud.io/summary/overall?id=asreview-simulation. The same GitHub
Action also calculates code coverage and uploads the results to SonarCloud:
https://sonarcloud.io/component_measures?id=asreview-simulation&metric=coverage&view=list.

In addition to the GitHub Action, unit test coverage can be calculated and reported locally using:

```shell
# collect the data:
coverage run --branch --source=asreviewcontrib.simulation -m pytest tests/unit/

# print a report in the terminal:
coverage report

# write a html report to ./html
coverage html --directory=./html
```

## Publishing: Preparation

TODO

- unit tests pass
- api tests pass
- use cases tests pass
- mocked tests pass
- integration tests pass
- citation metadata is up to date
- version is consistent across the repository
- source dist can be built
- wheel dist can be built

## Publishing: Zenodo

The repository has a GitHub action `zenodraft.yml` which can be triggered manually to publish a snapshot
of the current repository contents (`main` branch) to Zenodo as a zipped archive. The workflow does not
finalize the resulting deposition on Zenodo, so that the repository admin has a chance to review the draft
deposition before making it final by pressing the "Publish" button on Zenodo.

## Publishing: GitHub

Click the "Draft a new release" button on the releases page
[https://github.com/asreview-simulation/asreview-simulation/releases](https://github.com/asreview-simulation/asreview-simulation/releases).
Making a release is not set up to also trigger the zenodraft workflow.

## Publishing: PyPI

TODO https://blog.pypi.org/posts/2023-05-25-securing-pypi-with-2fa/

## Known problems

1. Some models generate `results.sql` non-deterministically, making it difficult to test whether they are (still) doing
the right thing (`cls-lstm-base`, `cls-lstm-pool`, `cls-nn-2-layer`, `cls-rf`). As a workaround, the tests for these
classifiers do not compare the contents of `reviews/<review_id>/results.sql` at the moment.
2. Embedding file doesn't seem to get used during `asreview simulate`, so there is nothing to compare to
for `asreview simulation start`.

## Plugins

Command line functionality can be extended by plugins.

1. new balancer subcommands via entry point group `"asreview_simulation.bal"`
2. new classifier subcommands via entry point group `"asreview_simulation.cls"`
3. new extractor subcommands via entry point group `"asreview_simulation.fex"`
4. new querier subcommands via entry point group `"asreview_simulation.qry"`
5. new sampler subcommands via entry point group `"asreview_simulation.sam"`
6. new stopping subcommands via entry point group `"asreview_simulation.stp"`

## Plan

1. review / verify / update each model's pyll program with respect to number, name, and type of parameters
2. add visualization for each pyll program so users can see what distribution a parameter is drawn from
3. ~~construct null distribution with pyll programs~~
4. ~~updating default configuration with distribution sampled from pyll programs~~
5. ~~starting ReviewSimulate with sampled distribution from pyll + default~~
6. rating each result with an objective function, e.g. from datatools or homemade
7. closing the feedback loop by drawing new parameterizations based on the result from previous parameterizations,
e.g. using one of hyperopt's optimization methods

## notes

- https://stackoverflow.com/questions/70984166/why-naive-bayes-gives-results-and-on-training-and-test-but-gives-error-of-negati
