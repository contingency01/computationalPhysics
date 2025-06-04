"""Utility functions used throughout the notebooks."""


def _square(val):
    """Return the sum of squares for a number or a sequence."""
    if isinstance(val, (list, tuple)):
        return sum(v ** 2 for v in val)
    return val ** 2


def sumSquares(x, y):
    """Return ``x`` squared plus ``y`` squared.

    The original implementation only worked for numeric values.  Some
    notebooks pass lists or tuples, which used to raise ``TypeError``.
    This version transparently handles numbers as well as sequences.
    """
    return _square(x) + _square(y)
