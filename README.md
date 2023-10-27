# asreview-simulation

Command line interface to simulate an [ASReview](https://pypi.org/project/asreview) analysis using a variety
of classifiers, feature extractors, queriers, and balancers, which can all be configured to run with
custom parameterizations.

## Status

| Badge &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; | Description |
|-------|-------------|
| [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.8042547.svg)](https://doi.org/10.5281/zenodo.8042547) | Persistent identifier for archived snapshots of the software |
| [![linting](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml) | Linting (`isort` and `black`, via `pre-commit`) |
| [![testing](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml) | Unit tests, mocked tests, and integration tests on combinations of operating system, ASReview version, and Python version |

## Install

```shell
# generate a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install asreview-simulation and its dependencies
pip install git+https://github.com/asreview-tuning/asreview-simulation.git@0.1.0
```

## Quickstart

Print the help:

```shell
asreview simulation --help
```

Print the configuration:

```shell
asreview simulation print-settings
```

With pretty-printing:

```shell
asreview simulation print-settings --pretty
```

Start a simulation using the default combination of models (`sam-random`,
`bal-double`, `cls-nb`, `fex-tfidf`, `qry-max`, `stp-min`), each using its default
parameterization:

```shell
asreview simulation start --benchmark benchmark:van_de_Schoot_2017 --out ./project.asreview
```

Instead of a benchmark dataset, you can also supply your own data via the `--in` option, as follows:

```shell
asreview simulation start --in ./myfile.csv --out ./project.asreview
asreview simulation start --in ./myfile.ris --out ./project.asreview
asreview simulation start --in ./myfile.tsv --out ./project.asreview
asreview simulation start --in ./myfile.xlsx --out ./project.asreview
```

Using a different classifier strategy can be accomplished by using one of
the `cls-*` subcommands before issuing the `start` subcommand, e.g.:

```shell
asreview simulation \
    cls-logistic \
    start --benchmark benchmark:van_de_Schoot_2017 --out ./project.asreview
```

Subcommands can be chained together, for example using the logistic
classifier with the undersample balancer goes like this:

```shell
asreview simulation \
    cls-logistic \
    bal-undersample \
    start --benchmark benchmark:van_de_Schoot_2017 --out ./project.asreview
```

Most subcommands have their own parameterization. Check the help of a
subcommand with `--help` or `-h` for short, e.g.:

```shell
asreview simulation cls-logistic --help
```
The above command will print:

```shell
Usage: asreview simulation cls-logistic [OPTIONS]

  Configure the simulation to use Logistic Regression classifier

Options:
  --c FLOAT             hyperparameter  [default: 1.0]
  --class_weight FLOAT  hyperparameter  [default: 1.0]
  -f, --force           Force setting the querier configuration, even if that
                        means overwriting a previous configuration.
  -h, --help            Show this message and exit.

  This command is chainable with other commands. Chained commands are
  evaluated left to right; make sure to end the chain with the 'start'
  command, otherwise it may appear like nothing is happening.

  Please report any issues at:

  https://github.com/asreview-tuning/asreview-simulation/issues.
```

Passing parameters to a subcommand goes like this:

```shell
asreview simulation \
    cls-logistic --class_weight 1.1 \
    start --benchmark benchmark:van_de_Schoot_2017 --out ./project.asreview
```

By using individually parameterized, chained subcommands we can compose a
variety of configurations, e.g.:

```shell
asreview simulation \
    sam-random --n_included 10 --n_excluded 15            \
    fex-tfidf --ngram_max 2                               \
    cls-nb --alpha 3.823                                  \
    qry-max-random --mix_ratio 0.95 --n_instances 10      \
    bal-double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1 \
    stp-nq --n_queries 20                                 \
    start --benchmark benchmark:van_de_Schoot_2017 --out ./project.asreview
```

Chained commands are evaluated left to right; make sure to end the chain
with the `start` command, otherwise it may appear like nothing is happening.

Here is the list of subcommands:

```shell
start                Start the simulation
print-settings       Print settings
save-settings        Save settings
load-settings        Load settings
sam-handpicked       Handpicked prior sampler
sam-random           Random prior sampler
fex-doc2vec          Doc2Vec extractor
fex-embedding-idf    Embedding IDF extractor
fex-embedding-lstm   Embedding LSTM extractor
fex-sbert            SBERT extractor
fex-tfidf            TF-IDF extractor
cls-logistic         Logistic Regression classifier
cls-lstm-base        LSTM Base classifier
cls-lstm-pool        LSTM Pool classifier
cls-nb               Naive Bayes classifier
cls-nn-2-layer       2-layer Neural Net classifier
cls-rf               Random Forest classifier
cls-svm              Support Vector Machine classifier
qry-cluster          Cluster query strategy
qry-max              Max query strategy
qry-max-random       Mixed query strategy (Max and Random)
qry-max-uncertainty  Mixed query strategy (Max and Uncertainty)
qry-random           Random query strategy
qry-uncertainty      Uncertainty query strategy
bal-double           Double balancer
bal-simple           No balancer
bal-undersample      Undersample balancer
stp-min              'min' stopping rule
stp-none             No stopping rule
stp-nq               Number of queries based stopping rule
```
