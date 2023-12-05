from functools import cached_property
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Tuple
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import griddata
from asreviewcontrib.simulation._private.lib.all_model_config import AllModelConfig
from asreviewcontrib.simulation._private.lib.plotting.padding import Padding


class _DataDict:
    def __init__(self, values: Dict[str, List[Any]], show_params: List[str]):
        self._values = values
        self._shown_params = show_params

    @cached_property
    def constant_params(self) -> List[str]:
        the_list = list()
        for param in self.params:
            is_constant = len(set(self._values[param])) == 1
            if is_constant:
                the_list.append(param)
        return the_list

    @cached_property
    def variable_params(self) -> List[str]:
        return sorted(set(self.params) - set(self.constant_params))

    @cached_property
    def params(self) -> List[str]:
        return sorted(self._values.keys())

    @cached_property
    def shown_params(self) -> List[str]:
        return self._shown_params

    @cached_property
    def types(self) -> Dict[str, type]:
        d = {}
        for param in self.params:
            d.update({param: type(self._values[param][0])})
        return d

    @cached_property
    def values(self):
        return self._values


class TrellisHandles:
    def __init__(
        self,
        axes_handles: List[List[Optional[plt.Axes]]],
        show_params: List[str],
    ):
        self._axes = axes_handles
        self._show_params = show_params

    def get_axes_by_row_name(self, row_name: str = None) -> List[plt.Axes]:
        assert row_name is not None, "Need a name to identify the row of subaxes"
        assert row_name in self.show_params[:-1], f"{row_name} is not a valid name for a row"
        irow = self.show_params.index(row_name)
        return [col for col in self.axes[irow] if col is not None]

    def get_axes_by_col_name(self, col_name: str = None) -> List[plt.Axes]:
        assert col_name is not None, "Need a name to identify the column of subaxes"
        assert col_name in self.show_params[1:], f"{col_name} is not a valid name for a column"
        icol = self.show_params.index(col_name)
        return [row[icol] for row in self.axes if row[icol] is not None]

    def get_axes_by_names(self, row_name: str = None, col_name: str = None) -> plt.Axes:
        assert row_name is not None, "Need a name to identify the row of subaxes"
        assert row_name in self.show_params[:-1], f"{row_name} is not a valid name for a row"
        assert col_name is not None, "Need a name to identify the column of subaxes"
        assert col_name in self.show_params[1:], f"{col_name} is not a valid name for a column"
        irow = self.show_params.index(row_name)
        icol = self.show_params.index(col_name)
        assert icol > irow, "No axes at that position."
        return self._axes[irow][icol]

    @property
    def axes(self):
        return self._axes

    @property
    def show_params(self):
        return self._show_params


def _calc_data_dict(
    data: List[Tuple[AllModelConfig, float]],
    show_params: List[str],
) -> Tuple[_DataDict, List[float]]:
    """Manipulate the data such that it becomes easy to access all values pertaining to
    a given parameter, as opposed to all values pertaining to a given sample."""

    params = data[0][0].flattened().keys()
    d = {}
    for param in params:
        d.update({param: [models.flattened()[param] for models, _ in data]})
    return _DataDict(d, show_params), [score for _, score in data]


def _calc_rect(
    inner_padding: Padding = None,
    outer_padding: Padding = None,
    icol: int = None,
    irow: int = None,
    n: int = None,
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
        (1.0 - inner_padding.top - inner_padding.bottom) * cell_height,
    )


def _get_row_col_quads(data_dict: _DataDict):
    r = []
    for irow, row_name in enumerate(data_dict.shown_params):
        for icol, col_name in enumerate(data_dict.shown_params):
            if icol > irow:
                t = irow, row_name, icol, col_name
                r.append(t)
    return r


def _plot_response_surface(
    handles: List[List[Optional[plt.Axes]]],
    data_dict: _DataDict,
    scores: List[float],
):
    """Visualize the data as a rasterized image by interpolating from available
    points sampled in a given axes."""
    nbins = 100
    for irow, row_name, icol, col_name in _get_row_col_quads(data_dict):
        ax = handles[irow][icol]
        plt.axes(ax)
        if data_dict.types[row_name] not in [int, bool, float]:
            continue
        if data_dict.types[col_name] not in [int, bool, float]:
            continue
        xv = [float(elem) for elem in data_dict.values[col_name]]
        yv = [float(elem) for elem in data_dict.values[row_name]]
        # manipulate xv, yv and scores to fit the function signature of griddata
        points = np.array([[xi, yi] for xi, yi in zip(xv, yv)])
        values = np.array(scores)
        xv_target = np.linspace(*ax.get_xlim(), nbins)
        yv_target = np.linspace(*ax.get_ylim(), nbins)
        estimation_points = [[[xi, yi] for xi in xv_target] for yi in yv_target]
        estimated_scores = griddata(points, values, estimation_points, method="linear")
        ax.imshow(estimated_scores, aspect="auto", extent=(*ax.get_xlim(), *ax.get_ylim()), origin="lower")


def _plot_scatter(
    handles: List[List[Optional[plt.Axes]]],
    data_dict: _DataDict,
    scatter_kwargs=None,
) -> None:
    """Visualize the data as scatter plots in the axes that should
    have been prepared previously."""

    scatter_kwargs = scatter_kwargs or {
        "marker": "+",
        "c": "k",
    }
    for irow, row_name, icol, col_name in _get_row_col_quads(data_dict):
        plt.axes(handles[irow][icol])
        plt.scatter(data_dict.values[col_name], data_dict.values[row_name], **scatter_kwargs)


def _plot_text(data_dict: _DataDict, trellis_handles: TrellisHandles):
    s = ""
    for param in data_dict.constant_params:
        s += f"{param}: {data_dict.values[param][0]}\n"
    params_left = data_dict.shown_params[:2]
    bottom_left_axes = trellis_handles.get_axes_by_names(*params_left)
    bottom_left_bbox = bottom_left_axes.get_position()

    params_right = data_dict.shown_params[-2:]
    top_right_axes = trellis_handles.get_axes_by_names(*params_right)
    top_right_bbox = top_right_axes.get_position()

    h = top_right_bbox.y1 - 0.1

    rect = bottom_left_bbox.x0, 0.1, 0.1, h
    ax = plt.axes(rect)
    ax.set_ylim(1, 0)
    ax.set_axis_off()
    plt.text(0, 0, s, verticalalignment="top")


def _prep_axes(
    data_dict: _DataDict,
    inner: Padding,
    outer: Padding,
) -> List[List[Optional[plt.Axes]]]:
    """Prepare a grid of axes in preparation of any plotting that happens later on."""

    n = len(data_dict.shown_params)
    handles = [[None] * n for _ in range(n)]
    for irow, row_name, icol, col_name in _get_row_col_quads(data_dict):
        rect = _calc_rect(inner, outer, icol=icol, irow=irow, n=n)
        kwargs = {}
        if irow == 0:
            kwargs.update({"xlabel": col_name})
        else:
            kwargs.update({
                "sharex": handles[0][icol],
            })

        if icol - 1 == irow:
            kwargs.update({"ylabel": row_name})
        else:
            kwargs.update({
                "sharey": handles[irow][icol - 1],
            })

        # construct the axes at the location defined by 'rect'
        ax = plt.axes(rect, **kwargs)
        ax.xaxis.grid(True, linestyle="dashed")
        ax.yaxis.grid(True, linestyle="dashed")
        ax.set_axisbelow(True)

        # hide xticklabels and yticklabels for axes that are in the middle
        if irow > 0:
            for label in ax.get_xticklabels():
                label.set_visible(False)
        if icol > irow + 1:
            for label in ax.get_yticklabels():
                label.set_visible(False)

        # assign axes handle to return arument so users can manipulate them if need be
        handles[irow][icol] = ax
    return handles


def plot_trellis(
    data: List[Tuple[AllModelConfig, float]],
    show_params: List[str] = None,
    outer_padding: Padding = None,
    inner_padding: Padding = None,
    scatter_kwargs: dict = None,
    show_response_surface=True,
    show_text=True,
) -> TrellisHandles:
    """Visualize each combination of 2 parameters out of a user-provided list of parameters."""

    assert len(data) >= 1, "Need at least one sample"
    expected_params = data[0][0].flattened().keys()
    for irow, row in enumerate(data):
        actual_params = row[0].flattened().keys()
        # verify that all the data rows are samples in the same parameter space
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
    axes_handles = _prep_axes(data_dict, inner=inner, outer=outer)

    trellis_handles = TrellisHandles(axes_handles, show_params)

    # visualize the data
    _plot_scatter(axes_handles, data_dict, scatter_kwargs)

    if show_response_surface:
        _plot_response_surface(axes_handles, data_dict, scores)

    if show_text:
        _plot_text(data_dict, trellis_handles)

    return trellis_handles
