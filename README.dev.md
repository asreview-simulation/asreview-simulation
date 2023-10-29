# Developer notes

## Install

```shell
mkdir <a directory>
git clone https://github.com/asreview-tuning/asreview-simulation .
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

| prior sampling   | feature extractor    | classifier       | querier           | balancer          | stopping   |
|------------------|----------------------|------------------|-------------------|-------------------|------------|
| `sam_handpicked` | `fex_doc2vec`        | `cls_logistic`   | `qry_cluster`     | `bal_double`      | `stp_min`  |
| `sam_random`     | `fex_embeding_idf`   | `cls_lstm_base`  | `qry_max`         | `bal_simple`      | `stp_none` |
|                  | `fex_embedding_lstm` | `cls_lstm_pool`  | `qry_max_random`  | `bal_undersample` | `stp_nq`   |
|                  | `fex_sbert`          | `cls_nb`         | `qry_uncertainty` |                   |            |
|                  | `fex_tfidf`          | `cls_nn_2_layer` | `qry_random`      |                   |            |
|                  |                      | `cls_rf`         | `qry_uncertainty` |                   |            |
|                  |                      | `cls_svm`        |                   |                   |            |

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

Besides running locally, they can also be run on GitHub infrastructure by manually triggering the GitHub action
workflow `.github/workflows/testing.yml`. The workflow tests whether the tests pass for all combinations of operating
system (Windows, Linux, MacOS), asreview version (1.0.4, 1.1.1, 1.2.1), and python version (3.8, 3.9, 3.10, 3.11).

Currently, the `testing` workflow on GitHub:

1. skips the tests for `fex-embedding-lstm` and for `fex-embedding-idf`,
because the necessary `--embedding` file is not present at the time the workflow runs.
2. skips installing `tensorflow` and tests pertaining to `cls_nn_2_layer` on Python >= 3.11

### `tests/unit`

These tests are simple, quick to run, and mostly focus on whether the `asreview-simulation` subcommands manipulate the
state (`obj`) in the correct way. The idea of the "unit" in unit testing is that when the test fails, there is just one
thing that could have gone wrong. This is in contrast to other types of test, e.g. integration testing (see below).

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

## Publishing: Preparation

TODO

- unit tests pass
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
[https://github.com/asreview-tuning/asreview-simulation/releases](https://github.com/asreview-tuning/asreview-simulation/releases).
Making a release is not set up to also trigger the zenodraft workflow.

## Publishing: PyPI

TODO

- https://blog.pypi.org/posts/2023-05-25-securing-pypi-with-2fa/

## Known problems

1. Some models generate `results.sql` non-deterministically, making it difficult to test whether they are (still) doing
the right thing (`cls-lstm-base`, `cls-lstm-pool`, `cls-nn-2-layer`, `cls-rf`). As a workaround, the tests for these
classifiers do not compare the contents of `reviews/<review_id>/results.sql` at the moment.
2. Embedding file doesn't seem to get used during `asreview simulate`, so there is nothing to compare to
for `asreview simulation start`.

### Hyperspace definition discrepancies

There are some discrepancies between the Python interface, the documentation, and the hyperspace definitions. What
follows is an overview of all models, along with how they define the number, name and type of their parameters in
their constructor, in their documentation, and in their `.full_hyper_space` functions. The tables below are based
on ASReview 1.2.

#### `DoubleBalance`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `a`    : float              | `a`    : float                     | `bal_a`    : float                  |
| `alpha`: float              | `alpha`: float                     | `bal_alpha`: float                  |
| `b`    : float              | `b`    : float                     | `bal_b`    : float                  |
| `beta` : float              | `beta` : float                     |                                     |
| `random_state`              |                                    |                                     |

#### `SimpleBalance`

no params

#### `UndersampleBalance`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `ratio`: float              | `ratio`: double                    | `bal_ratio`: float                  |
| `random_state`              |                                    |                                     |

#### `LogisticClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `C`           : float       | `C`           : float              | `mdl_C`            : float          |
| `class_weight`: float       | `class_weight`: float              | `mdl_class_weight` : float          |
| `random_state`              | `random_state`: int, RandomState   |                                     |
| `n_jobs`      : int         | `n_jobs`      : int                |                                     |

#### `LSTMBaseClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `embedding_matrix`          | `embedding_matrix`: numpy.ndarray  |                                     |
| `backwards`     : bool      | `backwards`       : bool           |                                     |
| `dropout`       : float     | `dropout`         : float          | `mdl_dropout`: float                |
| `optimizer`     : str       | `optimizer`       : str            |                                     |
| `lstm_out_width`: int       | `lstm_out_width`  : int            | `mdl_lstm_out_width`: int as float  |
| `learn_rate`    : float     | `learn_rate`      : float          | `mdl_learn_rate_mult`: float        |
| `dense_width`   : int       | `dense_width`     : int            | `mdl_dense_width` int as float      |
| `verbose`       : int       | `verbose`         : int            |                                     |
| `batch_size`    : int       | `batch_size`      : int            |                                     |
| `epochs`        : int       | `epochs`          : int            |                                     |
| `shuffle`       : bool      | `shuffle`         : bool           |                                     |
| `class_weight`  : float     | `class_weight`    : float          |                                     |

#### `LSTMPoolClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `embedding_matrix`          | `embedding_matrix`: numpy.ndarray  |                                     |
| `backwards`     : bool      | `backwards`       : bool           |                                     |
| `dropout`       : float     | `dropout`         : float          | `mdl_dropout`: float                |
| `optimizer`     : str       | `optimizer`       : str            |                                     |
| `lstm_out_width`: int       | `lstm_out_width`  : int            | `mdl_lstm_out_width`: int as float  |
| `lstm_pool_size`            | `lstm_pool_size`  : int            |                                     |
| `learn_rate`    : float     | `learn_rate`      : float          | `mdl_learn_rate_mult`: float        |
| `verbose`       : int       | `verbose`         : int            |                                     |
| `batch_size`    : int       | `batch_size`      : int            |                                     |
| `epochs`        : int       | `epochs`          : int            |                                     |
| `shuffle`       : bool      | `shuffle`         : bool           |                                     |
| `class_weight`  : float     | `class_weight`    : float          |                                     |
|                             |                                    | `mdl_dense_width`: int as float     |

#### `NaiveBayesClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `alpha`: float              | `alpha`: float                     | `mdl_alpha`: float                  |

#### `NN2LayerClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `dense_width`   : int       | `dense_width`   : int              | `mdl_dense_width` int as float      |
| `optimizer`     : str       | `optimizer`     : str              | `mdl_optimizer` choice of str       |
| `learn_rate`    : float     | `learn_rate`    : float            | `mdl_learn_rate` float              |
| `regularization`: float     | `regularization`: float            | `mdl_regularization` float          |
| `verbose`       : int       | `verbose`       : int              |                                     |
| `epochs`        : int       | `epochs`        : int              | `mdl_epochs` int as float           |
| `batch_size`    : int       | `batch_size`    : int              |                                     |
| `shuffle`       : bool      | `shuffle`       : bool             |                                     |
| `class_weight`  : float     | `class_weight`  : float            | `mdl_class_weight` float            |

#### `RandomForestClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `n_estimators`: int         | `n_estimators` : int               | `mdl_n_estimators` int as float     |
| `max_features`: int         | `max_features` : int               | `mdl_max_features` int as float     |
| `class_weight`: float       | `class_weight` : float             | `mdl_class_weight` float            |
| `random_state`              | `random_state` : int, RandomState  |                                     |

#### `SvmClassifier`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `gamma`       : str         | `gamma`        : str               | `mdl_gamma`       : choice of str   |
| `class_weight`: float       | `class_weight` : float             | `mdl_class_weight`: float           |
| `C`           : float       | `C`            : float             | `mdl_C`           : float           |
| `kernel`      : str         | `kernel`       : str               | `mdl_kernel`      : choice of str   |
| `random_state`              | `random_state` : int, RandomState  |                                     |

#### `Doc2Vec`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `split_ta`    : int         | -                                  | `fex_split_ta`    : int             |
| `use_keywords`: int         | -                                  | `fex_use_keywords`: int             |
| `vector_size` : int         | `vector_size`: int                 | `fex_vector_size` : int as float    |
| `epochs`      : int         | `epochs`     : int                 | `fex_epochs`      : int as float    |
| `min_count`   : int         | `min_count`  : int                 | `fex_min_count`   : int as float    |
| `n_jobs`      : int         | `n_jobs`     : int                 |                                     |
| `window`      : int         | `window`     : int                 | `fex_window`      : int as float    |
| `dm_concat`   : int         | `dm_concat`  : int                 | `fex_dm_concat`   : int             |
| `dm`          : int         | `dm`         : int                 | `fex_dm`          : int             |
| `dbow_words`  : int         | `dbow_words` : int                 | `fex_dbow_words`  : int             |

#### `EmbeddingIdf`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `split_ta`    : int         | -                                  | `fex_split_ta`    : int             |
| `use_keywords`: int         | -                                  | `fex_use_keywords`: int             |
| `random_state`              |                                    |                                     |

#### `EmbeddingLSTM`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `split_ta`            : int | -                                  | `fex_split_ta`      : int           |
| `use_keywords`        : int | -                                  | `fex_use_keywords`  : int           |
| `loop_sequence`       : int | `loop_sequence`       : bool       | `fex_loop_sequences`: int           |
| `num_words`           : int | `num_words`           : int        |                                     |
| `max_sequence_length` : int | `max_sequence_length` : int        |                                     |
| `padding`             : str | `padding`             : str        |                                     |
| `truncating`          : str | `truncating`          :            |                                     |
| `n_jobs`              : int | `n_jobs`                           |                                     |

#### `SBERT`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `split_ta`         : int    | -                                  | `fex_split_ta`    : int             |
| `use_keywords`     : int    | -                                  | `fex_use_keywords`: int             |
| `transformer_model`: str    | `transformer_model`: str           |                                     |

#### `Tfidf`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `split_ta`    : int         | -                                  | `fex_split_ta`    : int             |
| `use_keywords`: int         | -                                  | `fex_use_keywords`: int             |
| `ngram_max`   : int         | `ngram_max`: int                   | `fex_ngram_max`   : int             |
| `stop_words`  : str         | `stop_words`: str                  | `fex_stop_words`  : choice of str   |

#### `ClusterQuery`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `cluster_size`   : int      | `cluster_size`: int                | `qry_cluster_size`   : int as float |
| `update_interval`: int      | `update_interval`: int             | `qry_update_interval`: int as float |
| `random_state`              | `random_state` : int, RandomState  |                                     |

#### `MaxQuery`

no params

#### `MixedQuery`

| constructor                 | documentation                      | `.full_hyper_space()`               |
|-----------------------------|------------------------------------|-------------------------------------|
| `strategy_1`: str           | `strategy_1`   : str               |                                     |
| `strategy_2`: str           | `strategy_2`   : str               |                                     |
| `mix_ratio` : float         | `mix_ratio`    : float             | `qry_mix_ratio`: float              |
| `random_state`              | `random_state` : float             |                                     |
| `kwargs`                    | `kwargs`       : dict              | `qry_<strategy_1>_*` (dynamic)      |
| `kwargs`                    | `kwargs`       : dict              | `qry_<strategy_2>_*` (dynamic)      |

#### `RandomQuery`

no params

#### `UncertaintyQuery`

no params

## Plan

1. construct null distribution with pyll programs
2. update default configuration with distribution sampled from pyll programs
3. start ReviewSimulate with sampled distribution from pyll + default
4. rate each result with an objective function, e.g. from datatools or homemade
5. verify / update each model's pyll program
6. visualize each model

## notes

- https://stackoverflow.com/questions/70984166/why-naive-bayes-gives-results-and-on-training-and-test-but-gives-error-of-negati
- provides a standalone CLI command `asreview-simulation`
- provides a plugin to `asreview` where it will show up as the subcommand `simulation` so users can call `asreview simulation` (i.e. without the dash)
- its functionality can be extended by plugins:
    - new balancer subcommands via entry point group `"asreview_simulation.balancers"`
    - new classifier subcommands via entry point group `"asreview_simulation.classifiers"`
    - new extractor subcommands via entry point group `"asreview_simulation.extractors"`
    - new querier subcommands via entry point group `"asreview_simulation.queriers"`
