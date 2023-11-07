from asreview.models.query.random import RandomQuery


def qry_random_unwrap(_params, random_state):
    return RandomQuery(random_state=random_state)
