# A fresh take on ASReview's project layout

Each directory here is supposed to be represent a published package from pypi. Their directory names are the package names.
Since none of the packages are actually published you have to install them with e.g. `pip install -e ./asreviewlib`

- `asreview`:
    - provides an initially empty `asreview` CLI command 
    - its functionality can be extended by plugins that supply subcommands via entry point group `"asreview.subcommands"`   
- `asreview-simulation`:
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
    - see detailed help in [the appendix](#appendix-asreview-simulation-cli)
- `asreview-simulation-plugin-extractor`:
    - provides a plugin to `asreview-simulation` where it will show up as a new subcommand `ext:new` so users can call e.g. `asreview simulation ext:new print-settings --pretty`
- `asreviewlib`:
    - currently just an interface library with no implementation
    - demonstrates what the API should be (see list below [#appendix: asreviewlib-api](#appendix-asreviewlib-api))
    - its functionality can be extended by plugins:
        - new balancers via entry point group `"asreviewlib.balancers"`
        - new classifiers via entry point group `"asreviewlib.classifiers"`
        - new datasets via entry point group `"asreviewlib.datasets"`
        - new extractors via entry point group `"asreviewlib.extractors"`
        - new queriers via entry point group `"asreviewlib.queriers"`
        - new readers via entry point group `"asreviewlib.readers"`
        - new writers via entry point group `"asreviewlib.writers"`
- `asreviewlib-plugin-classifier`:
    - provides a plugin to `asreviewlib` where it will show up as a new classifier `NewClassifier` to be used in Python code, e.g.:

        ```shell
        $ python3
        >>> from asreviewlib import  list_classifiers
        >>> for item in list_classifiers(): print(item)
        ...
        logistic
        lstm-base
        lstm-pool
        nb
        nn-2-layer
        rf
        svm

        Ctrl-D

        $ pip install -e ./asreviewlib-plugin-classifier
        $ python3
        >>> from asreviewlib import list_classifiers
        >>> for item in list_classifiers(): print(item)
        ...
        logistic
        lstm-base
        lstm-pool
        nb
        new
        nn-2-layer
        rf
        svm
        ```
- `asreviewlib-plugin-dataset`:
    - provides a plugin to `asreviewlib` where it will show up as a new dataset `ThirdDataset` to be used in Python code, e.g.:

        ```shell
        $ python3
        >>> from asreviewlib import  list_datasets
        >>> for item in list_datasets(): print(item)
        ...
        first
        second

        Ctrl-D

        $ pip install -e ./asreviewlib-plugin-dataset
        $ python3
        >>> from asreviewlib import list_datasets
        >>> for item in list_datasets(): print(item)
        ...
        first
        second
        third
        ```
- `privacy-patterns-1`
    - illustrates the pattern that `asreview-1.1.1` has which unintentionally exposes a lot of the internals

        ```shell
        python3 -m venv venv
        source venv/bin/activate
        pip install -e ./privacy-pattern-1[testing]
        python3
        >>> import privacy_patterns_1
        >>> privacy_patterns_1.demo.fun()  # works fine, prints:
        module privacy_patterns_1.demo imports built-in module 'sys': <module 'sys' (built-in)>
        >>> dir(privacy_patterns_1.demo)   # indeed lists 'demo' but also unwanted 'sys'
        Ctrl-D
        $ pytest ./privacy-patterns-1      # should fail with messages about sys
        ```
- `privacy-patterns-2`
    - illustrates a pattern that helps avoid unintentionally exposing internals

        ```
        pip install -e ./privacy-patterns-2[testing]
        python3
        >>> import privacy_patterns_2
        >>> privacy_patterns_2.demo.fun()  # works fine, prints:
        module privacy_patterns_2.demo._demo imports built-in module 'sys': <module 'sys' (built-in)>
        >>> dir(privacy_patterns_2.demo)   # indeed lists 'demo' but not 'sys'
        Ctrl-D
        $ pytest ./privacy-patterns-2      # passes
        ```
- `privacy-patterns-3`
    - illustrates a pattern that helps avoid unintentionally exposing internals

        ```shell
        $ pip install -e privacy-patterns-3[testing]
        $ pytest ./privacy-patterns-3 # should pass but the api includes
                                      # one private member, '_internal'
        ```


## Appendix `asreview-simulation` CLI

### Print the help:

```shell
$ asreview-simulation
Usage: asreview-simulation [OPTIONS] COMMAND1 [ARGS]... [COMMAND2
                           [ARGS]...]...

  Example usage:

    $ asreview-simulation print-settings

    $ asreview-simulation start --data labeled-records.db

  Commands can be chained together, e.g.

    $ asreview-simulation load-settings thefile.cfg start --data labeled-
    records.db

    $ asreview-simulation load-settings thefile.cfg start --dataset second

    $ asreview-simulation bal:double --alpha 1.23 print-settings --pretty

    $ asreview-simulation bal:none cls:nb ext:tfidf qer:mixed start --data
    labeled-records.db

    $ asreview-simulation sam:random --n_included 10 --n_excluded 15                      \
                          ext:tfidf --ngram_max 2                                         \
                          cls:nb --alpha 3.823                                            \
                          qer:mixed --strategy1 max --strategy2 random --mix_ratio 0.95   \
                          bal:double --a 2.156 --alpha 0.95 --b 0.79 --beta 1.1           \
                          start --data labeled-records.db

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
            "ngrams_max": 1,
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
  --shuffle       hyperparameter 'shuffle'.
  -h, --help      Show this message and exit.

  This command is chainable with other commands. Chained commands are
  evaluated left to right; make sure to end the chain with either a 'start'
  command or a 'print-settings' command, otherwise it may appear like nothing
  is happening.
```

### Chaining subcommands

Change the settings by chaining subcommands. Chain with the print command at the end to see them in the terminal:

```shell
$ asreview-simulation bal:undersample --ratio 0.5 cls:rf --class_weight 1.0001 print-settings --pretty                                                         
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
            "class_weight": 1.0001,
            "max_features": 10,
            "n_estimators": 100,
            "seed": 535
        }
    },
    "extractor": {
        "model": "tfidf",
        "params": {
            "ngrams_max": 1,
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


## Appendix: `asreviewlib` API

See [`asreviewlib/test/test_api.py`](asreviewlib/tests/test_api.py) for the complete and up to date programming interface.

```text
asreviewlib.balancers.BaseBalancer
asreviewlib.balancers.DoubleBalancer
asreviewlib.balancers.NoneBalancer
asreviewlib.balancers.TripleBalancer
asreviewlib.balancers.UndersampleBalancer
asreviewlib.balancers
asreviewlib.BaseModel
asreviewlib.classifiers.BaseClassifier
asreviewlib.classifiers.LogisticClassifier
asreviewlib.classifiers.LstmBaseClassifier
asreviewlib.classifiers.LstmPoolClassifier
asreviewlib.classifiers.NaiveBayesClassifier
asreviewlib.classifiers.NN2LayerClassifier
asreviewlib.classifiers.RandomForestClassifier
asreviewlib.classifiers.SvmClassifier
asreviewlib.classifiers
asreviewlib.Data
asreviewlib.exceptions.ASReviewProjectExistsError
asreviewlib.exceptions.ASReviewProjectNotFoundError
asreviewlib.exceptions
asreviewlib.extractors.BaseExtractor
asreviewlib.extractors.Doc2VecExtractor
asreviewlib.extractors.EmbeddingIdfExtractor
asreviewlib.extractors.EmbeddingLstmExtractor
asreviewlib.extractors.SbertExtractor
asreviewlib.extractors.TfidfExtractor
asreviewlib.extractors
asreviewlib.list_balancers
asreviewlib.list_classifiers
asreviewlib.list_extractors
asreviewlib.list_projects
asreviewlib.list_queriers
asreviewlib.list_readers
asreviewlib.list_writers
asreviewlib.Project
asreviewlib.queriers.BaseQuerier
asreviewlib.queriers.ClusterQuerier
asreviewlib.queriers.MaxQuerier
asreviewlib.queriers.MaxRandomQuerier
asreviewlib.queriers.MaxUncertaintyQuerier
asreviewlib.queriers.MixedQuerier
asreviewlib.queriers.RandomQuerier
asreviewlib.queriers.UncertaintyQuerier
asreviewlib.queriers
asreviewlib.readers.CsvReader
asreviewlib.readers.RisReader
asreviewlib.readers.TsvReader
asreviewlib.readers.XlsReader
asreviewlib.readers
asreviewlib.state.create_database
asreviewlib.state.create_event
asreviewlib.state.create_record
asreviewlib.state.delete_database
asreviewlib.state.delete_event
asreviewlib.state.delete_record
asreviewlib.state.read_database
asreviewlib.state.read_event
asreviewlib.state.read_record
asreviewlib.state.update_database
asreviewlib.state.update_event
asreviewlib.state.update_record
asreviewlib.state
asreviewlib.writers.CsvWriter
asreviewlib.writers.RisWriter
asreviewlib.writers.TsvWriter
asreviewlib.writers.XlsWriter
asreviewlib.writers
```
