from typing import List
from typing import Tuple
from typing import Dict
from typing import Optional
from typing import Any
from matplotlib import pyplot as plt
from asreviewcontrib.simulation._private.lib.all_model_config import AllModelConfig
from asreviewcontrib.simulation._private.lib.plotting.padding import Padding


def _calc_data_dict(
    data: List[Tuple[AllModelConfig, float]],
    param_names: List[str]
) -> Tuple[Dict[str, List[Any]], List[float]]:
    """Manipulate the data such that it becomes easy to access all values pertaining to
    a given parameter, as opposed to all values pertaining to a given sample."""

    flatteneds = [(models.flattened(), score) for models, score in data]
    d = {}
    for param_name in param_names:
        d.update({param_name: [flat[param_name] for flat, _ in flatteneds]})
    return d, [score for _, score in flatteneds]


def _calc_rect(
    inner_padding: Padding = None,
    outer_padding: Padding = None,
    icol: int = None,
    irow: int = None,
    n: int = None
) -> Tuple[float, float, float, float]:
    """Given some information about padding, calculate the coordinates that a given
    axes would occupy given its row index, column index, and the number of axes on
    each row and column."""

    inner_padding = inner_padding or Padding()
    outer_padding = outer_padding or Padding()
    cell_width = (1.0 - outer_padding.left - outer_padding.right) / (n - 1)
    cell_height = (1.0 - outer_padding.top - outer_padding.bottom) / (n - 1)
    return (
        outer_padding.left + (icol - 1) * cell_width + inner_padding.left * cell_width,
        outer_padding.bottom + irow * cell_height + inner_padding.bottom * cell_height,
        (1.0 - inner_padding.left - inner_padding.right) * cell_width,
        (1.0 - inner_padding.top - inner_padding.bottom) * cell_height
    )


def _plot_response_surface(handles: List[List[Optional[plt.Axes]]],
                           data_dict: Dict[str, List[Optional[Any]]],
                           scores: List[Any]):
    """Visualize the data as a rasterized image by interpolating from available
    points sampled in a given axes."""
    raise NotImplementedError


def _plot_scatter(
    handles: List[List[Optional[plt.Axes]]],
    data_dict: Dict[str, List[Optional[Any]]],
    show_params: List[str],
    scatter_kwargs
) -> None:
    """Visualize the data as scatter plots in the axes that should
    have been prepared previously."""

    for irow, row_name in enumerate(show_params):
        for icol, col_name in enumerate(show_params):
            if icol > irow:
                plt.axes(handles[irow][icol])
                plt.scatter(data_dict[col_name], data_dict[row_name], **scatter_kwargs)


def _prep_axes(
    show_params: List[str],
    inner: Padding,
    outer: Padding
) -> List[List[Optional[plt.Axes]]]:
    """Prepare a grid of axes in preparation of any plotting that happens later on."""

    n = len(show_params)
    handles = [[None] * n for _ in range(n)]
    for irow, _ in enumerate(show_params):
        for icol, _ in enumerate(show_params):
            if icol > irow:
                rect = _calc_rect(inner, outer, icol=icol, irow=irow, n=n)
                kwargs = {}
                if irow == 0:
                    kwargs.update({"xlabel": show_params[icol]})
                else:
                    kwargs.update({"xticklabels": []})

                if icol - 1 == irow:
                    kwargs.update({"ylabel": show_params[irow]})
                else:
                    kwargs.update({"yticklabels": []})

                ax = plt.axes(rect, **kwargs)
                ax.xaxis.grid(True, linestyle="dashed")
                ax.yaxis.grid(True, linestyle="dashed")
                ax.set_axisbelow(True)
                handles[irow][icol] = ax
    return handles


def plot_trellis(
    data: List[Tuple[AllModelConfig, float]],
    show_params: List[str] = None,
    outer_padding: Padding = None,
    inner_padding: Padding = None,
    show_scatter=True,
    scatter_kwargs: dict = None,
    show_response_surface=True
) -> List[List[Optional[plt.Axes]]]:
    """Visualize each combination of 2 parameters out of a user-provided list of parameters."""

    # verify that all the data rows are samples in the same parameter space
    expected_params = data[0][0].flattened().keys()
    for irow, row in enumerate(data):
        actual_params = row[0].flattened().keys()
        assert set(actual_params) == set(expected_params), f"Data row {irow} has unexpected key set"

    # verify that the parameters selected for plotting are in fact all present
    show_params = show_params or sorted(expected_params)
    assert set(show_params).issubset(set(expected_params)), "The data doesn't include all the parameters you wanted to plot"

    data_dict, scores = _calc_data_dict(data, show_params)

    # assign defaults
    outer = outer_padding or Padding(left=0.14, right=0.01, top=0.01, bottom=0.14)
    inner = inner_padding or Padding(left=0.05, right=0.05, top=0.05, bottom=0.05)
    scatter_kwargs = scatter_kwargs or {}

    # prepare the grid of axes
    axes_handles = _prep_axes(show_params, inner=inner, outer=outer)

    # visualize the data
    if show_scatter:
        _plot_scatter(axes_handles, data_dict, show_params, scatter_kwargs)

    if show_response_surface:
        _plot_response_surface(axes_handles, data_dict, scores)

    return axes_handles
