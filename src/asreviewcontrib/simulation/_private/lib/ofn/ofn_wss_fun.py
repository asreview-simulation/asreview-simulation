from asreview import open_state
from asreviewcontrib.insights.metrics import wss


def ofn_wss_fun(project_path, at_perc):
    assert 0 <= at_perc <= 100, "Expected value of input argument 'at_perc' to be in interval [0,100]"
    with open_state(project_path, read_only=True) as s:
        return wss(s, at_perc / 100, priors=False, x_absolute=False, y_absolute=False)
