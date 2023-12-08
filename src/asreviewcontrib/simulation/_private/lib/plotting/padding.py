class Padding:
    """
    Class to keep track of padding length in 4 directions: `bottom`, `left`, `right`, `top`.
    """
    def __init__(self, bottom: float = 0.1, left: float = 0.1, right: float = 0.1, top: float = 0.1):
        """
        Synopsis:

            Constructor method.

        Example usage:

            Use the default lengths of 0.1 all around:
            ```python
            from asreviewcontrib.simulation.api.plotting import Padding


            padding = Padding()
            ```

            Use 0.0 padding horizontally and 0.2 vertically:

            ```python
            from asreviewcontrib.simulation.api.plotting import Padding


            padding = Padding(left=0.0, right=0.0, top=0.2, bottom=0.2)
            ```
        """
        # define private attributes
        self._bottom = None
        self._left = None
        self._right = None
        self._top = None

        # set private attributes via setters
        self.bottom = bottom
        self.left = left
        self.right = right
        self.top = top

    @property
    def bottom(self):
        """
        The padding length at the bottom side.
        """
        return self._bottom

    @bottom.setter
    def bottom(self, bottom):
        """
        The padding length at the bottom side.
        """
        self._bottom = bottom

    @property
    def left(self):
        """
        The padding length at the left side.
        """
        return self._left

    @left.setter
    def left(self, left):
        """
        The padding length at the left side.
        """
        self._left = left

    @property
    def right(self):
        """
        The padding length at the right side.
        """
        return self._right

    @right.setter
    def right(self, right):
        """
        The padding length at the right side.
        """
        self._right = right

    @property
    def top(self):
        """
        The padding length at the top side.
        """
        return self._top

    @top.setter
    def top(self, top):
        """
        The padding length at the top side.
        """
        self._top = top
