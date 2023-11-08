from asreview.models.query.random import RandomQuery


def instantiate_unwrapped_qry_random(_params, random_state):
    return RandomQuery(random_state=random_state)
