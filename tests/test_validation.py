"""
test_validation.py

Tests for validation metrics such as RMSE and percent error.
Ensures correctness of comparison functions.
"""

import numpy as np
from validation import rmse, percent_error


def test_rmse_zero():
    """
    RMSE should be zero when two arrays are identical.
    """
    a = np.array([1, 2, 3])

    assert rmse(a, a) == 0


def test_percent_error_zero():
    """
    Percent error should be zero when arrays match exactly.
    """
    a = np.array([1, 2, 3])

    assert percent_error(a, a) == 0


def test_rmse_positive():
    """
    RMSE should be positive when arrays differ.
    """
    a = np.array([1, 2, 3])
    b = np.array([2, 3, 4])

    assert rmse(a, b) > 0
