[![linting](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/linting.yml)
[![testing](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml/badge.svg)](https://github.com/asreview-tuning/asreview-simulation/actions/workflows/testing.yml)

# asreview-simulation

- provides a standalone CLI command `asreview-simulation`
- provides a plugin to `asreview` where it will show up as the subcommand `simulation` so users can call `asreview simulation` (i.e. without the dash)
- its functionality can be extended by plugins:
    - new balancer subcommands via entry point group `"asreview_simulation.balancers"`
    - new classifier subcommands via entry point group `"asreview_simulation.classifiers"`
    - new extractor subcommands via entry point group `"asreview_simulation.extractors"`
    - new querier subcommands via entry point group `"asreview_simulation.queriers"`
    - new sampler subcommands via entry point group `"asreview_simulation.samplers"`
    - new starter via entry point group `"asreview_simulation.starters"`
    - new terminator subcommands via entry point group `"asreview_simulation.terminators"`
- see detailed help below

### Print the help:

```shell
$ asreview-simulation
Usage: asreview-simulation [OPTIONS] COMMAND1 [ARGS]... [COMMAND2
                           [ARGS]...]...

  Example usage:

    $ asreview-simulation print-settings

    $ asreview-simulation start --data labeled-records.csv

  Commands can be chained together, e.g.

    $ asreview-simulation load-settings thefile.json start --data labeled-
    records.csv

    $ asreview-simulation load-settings thefile.json start --dataset benchmark:van_de_Schoot_2017

    $ asreview-simulation bal:double --alpha 1.23 print-settings --pretty

    $ asreview-simulation bal:none cls:nb ext:tfidf qer:mixed start --data
    labeled-records.csv

    $ asreview-simulation sam:random --n_included 10 --n_excluded 15                      \
                          ext:tfidf --ngram_max 2                                         \
                          cls:nb --alpha 3.823                                            \
                          qer:mixed --strategy1 max --strategy2 random --mix_ratio 0.95   \
                          bal:double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1           \
                          start --data labeled-records.csv

  Chained commands are evaluated left to right; make sure to end the chain
  with either a 'start' command or a 'print-settings' command, otherwise it
  may appear like nothing is happening.

Options:
  -h, --help  Show this message and exit.

Commands:
  load-settings       Load settings
  sam:handpicked      Use handpicked prior sampler
  sam:random          Use random prior sampler
  bal:double          Use double balancer
  bal:none            Use no balancer
  bal:triple          Use triple balancer
  bal:undersample     Use undersample balancer
  cls:logistic        Use Logistic Regression classifier
  cls:lstm-base       Use LSTM Base classifier
  cls:lstm-pool       Use LSTM Pool classifier
  cls:nb              Use Naive Bayes classifier
  cls:nn-2-layer      Use 2-layer Neural Net classifier
  cls:rf              Use Random Forest classifier
  cls:svm             Use Support Vector Machine classifier
  ext:doc2vec         Use Doc2Vec extractor
  ext:embedding-idf   Use Embedding IDF extractor
  ext:embedding-lstm  Use Embedding LSTM extractor
  ext:new             Use a new extractor
  ext:sbert           Use SBERT extractor
  ext:tfidf           Use TF-IDF extractor
  qer:cluster         Use Cluster querier
  qer:mixed           Use Mixed querier
  print-settings      Print settings
  save-settings       Save settings
  start               Start the simulation and exit; terminates parsing
```

### Print the default settings:

```shell
$ asreview-simulation print-settings --pretty
```
```json
{
    "balancer": {
        "model": "double",
        "params": {
            "a": 2.155,
            "alpha": 0.94,
            "b": 0.789,
            "beta": 1.0
        }
    },
    "classifier": {
        "model": "nb",
        "params": {
            "alpha": 3.822
        }
    },
    "extractor": {
        "model": "tfidf",
        "params": {
            "ngram_max": 1,
            "stop_words": "english"
        }
    },
    "querier": {
        "model": "max",
        "params": {}
    },
    "sampler": {
        "model": "random",
        "params": {
            "n_excluded": 1,
            "n_included": 1
        }
    }
}
```

### Print the help for a subcommand

e.g. for triple balancer:

```shell
$ asreview-simulation bal:triple --help
Usage: asreview-simulation bal:triple [OPTIONS]

  Use triple balancer

Options:
  --a FLOAT       hyperparameter  [default: 2.155]
  --alpha FLOAT   hyperparameter  [default: 0.94]
  --b FLOAT       hyperparameter  [default: 0.789]
  --beta FLOAT    hyperparameter  [default: 1.0]
  --c FLOAT       hyperparameter  [default: 0.835]
  -f, --force     Force setting the querier configuration, even if that means
                  overwriting a previous configuration.
  --gamma FLOAT   hyperparameter  [default: 2.0]
  --seed INTEGER  Random seed  [default: 535]
  --shuffle       hyperparameter
  -h, --help      Show this message and exit.

  This command is chainable with other commands. Chained commands are
  evaluated left to right; make sure to end the chain with either a 'start'
  command or a 'print-settings' command, otherwise it may appear like nothing
  is happening.
```

### Chaining subcommands

Change the settings by chaining subcommands. Chain with the print command at the end to see them in the terminal:

```shell
$ asreview-simulation bal:undersample --ratio 0.5 cls:rf --class_weight 1.01 print-settings --pretty
```
```json
{
    "balancer": {
        "model": "undersample",
        "params": {
            "ratio": 0.5,
            "seed": 535
        }
    },
    "classifier": {
        "model": "rf",
        "params": {
            "class_weight": 1.01,
            "max_features": 10,
            "n_estimators": 100,
            "seed": 535
        }
    },
    "extractor": {
        "model": "tfidf",
        "params": {
            "ngram_max": 1,
            "stop_words": "english"
        }
    },
    "querier": {
        "model": "max",
        "params": {}
    },
    "sampler": {
        "model": "random",
        "params": {
            "n_excluded": 1,
            "n_included": 1
        }
    }
}
```
