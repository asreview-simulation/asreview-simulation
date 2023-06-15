[![linting](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml)
[![testing](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml)

# asreview-simulation

## Install

```shell
# generate a virtual environment
python3 -m venv venv

# activate the virtual environment
source venv/bin/activate

# install asreview-simulation and its dependencies
pip install git+https://github.com/asreview-tuning/asreview-simulation.git
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

Start a simulation using the default combination of models (`sam:random`,
`bal:double`, `cls:nb`, `fex:tfidf`, `qry:max`, `stp:min`), each using its default
parameterization:

```shell
asreview simulation start --dataset benchmark:van_de_Schoot_2017 ./project.asreview
```

Using a different classifier strategy can be accomplished by using one of
the `cls:*` subcommands before issuing the `start` subcommand, e.g.:

```shell
asreview simulation cls:logistic start --dataset benchmark:van_de_Schoot_2017 ./project.asreview
```

Subcommands can be chained together, for example using the logistic
classifier with the undersample balancer goes like this:

```shell
asreview simulation cls:logistic bal:undersample \
                    start --dataset benchmark:van_de_Schoot_2017 ./project.asreview
```

Most subcommands have their own parameterization. Check the help of a
subcommand with `--help` or `-h` for short, e.g.:

```shell
asreview simulation cls:logistic --help
```
The above command will print:

```shell
Usage: asreview simulation cls:logistic [OPTIONS]

  Use Logistic Regression classifier

Options:
  --c FLOAT             hyperparameter  [default: 1.0]
  --class_weight FLOAT  hyperparameter  [default: 1.0]
  -f, --force           Force setting the querier configuration, even if that
                        means overwriting a previous configuration.
  -h, --help            Show this message and exit.

  This command is chainable with other commands. Chained commands are
  evaluated left to right; make sure to end the chain with either a 'start'
  command or a 'print-settings' command, otherwise it may appear like nothing
  is happening.
```

Passing parameters to a subcommand goes like this:

```shell
asreview simulation cls:logistic --class_weight 1.1 \
                    start --dataset benchmark:van_de_Schoot_2017 ./project.asreview
```

By using individually parameterized, chained subcommands we can compose a
variety of configurations, e.g.:

```shell
asreview simulation sam:random --n_included 10 --n_excluded 15            \
                    fex:tfidf --ngram_max 2                               \
                    cls:nb --alpha 3.823                                  \
                    qry:max_random --mix_ratio 0.95 --n_instances 10      \
                    bal:double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1 \
                    stp:n 20                                              \
                    start --dataset benchmark:van_de_Schoot_2017 ./project.asreview
```

Chained commands are evaluated left to right; make sure to end the chain
with either a `start` command or a `print-settings` command, otherwise it
may appear like nothing is happening.

Here is the list of subcommands:

```shell
load-settings        Load settings
sam:handpicked       Use handpicked prior sampler
sam:random           Use random prior sampler
bal:double           Use double balancer
bal:simple           Use no balancer
bal:undersample      Use undersample balancer
cls:logistic         Use Logistic Regression classifier
cls:lstm-base        Use LSTM Base classifier
cls:lstm-pool        Use LSTM Pool classifier
cls:nb               Use Naive Bayes classifier
cls:nn-2-layer       Use 2-layer Neural Net classifier
cls:rf               Use Random Forest classifier
cls:svm              Use Support Vector Machine classifier
fex:doc2vec          Use Doc2Vec extractor
fex:embedding-idf    Use Embedding IDF extractor
fex:embedding-lstm   Use Embedding LSTM extractor
fex:sbert            Use SBERT extractor
fex:tfidf            Use TF-IDF extractor
qry:cluster          Use Cluster querier
qry:max              Use Max querier
qry:max_random       Mixed query strategy ('max' and 'random')
qry:max_uncertainty  Mixed query strategy ('max' and 'uncertainty')
qry:random           Random query
qry:uncertainty      Uncertainty query strategy
stp:min              Stop the simulation once all relevant records have...
stp:n                Stop the simulation after evaluating N queries,...
stp:none             Stop the simulation after evaluating all records,...
print-settings       Print settings
save-settings        Save settings
start                Start the simulation and write the results to a...
```
