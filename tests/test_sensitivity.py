"""
test_sensitivity.py

Tests for parameter variation used in sensitivity analysis.
"""

from sensitivity import vary_parameter


def test_vary_parameter_20_percent():
    """
    Ensure that varying a parameter by ±20% produces correct values.

    Example:
    10 → 8 (low), 12 (high)
    """
    low, high = vary_parameter(10, 0.2)

    # Check lower bound
    assert low == 8

    # Check upper bound
    assert high == 12
