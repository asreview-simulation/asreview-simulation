- [x] make it easy (e.g. via a CLI) to pick a combination of models and run with the default parameterization 
- [x] make it easy (e.g. via a CLI) to pick a combination of models and run with a custom parameterization 
- [x] add unit tests
- [x] add [mocked, integration] tests to compare the results from the new CLI (`asreview simulation`) with
      those from the old CLI (`asreview simulate`)
- [ ] investigate drawing random parameterizations, maybe using a randn on top of the default
      parameterization, or maybe even better using the range and distribution baked into each model via its `hyper_choices` and `hyper_pars`
- [ ] investigate rating a given result with an objective function, e.g. using some functions from the insights package.
- [ ] close the feedback loop by drawing new parameterizations, e.g. using one of hyperopt's optimization methods
