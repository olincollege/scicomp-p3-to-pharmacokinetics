"""
sensitivity.py

This file contains the sensitivity analysis for pharmacokinetic model robustness.
"""

# Importing in Needed Libraries
import numpy as np

from constants import CL, Vc, Vc, Q
from simulation import run_second_compartment


def vary_parameter(base_value, percent_change=0.2):
    """
    This function creates lower and upper values for ±percent variation.

    Args:
        base_value (float): original parameter
        percent_change (float): default 20%

    Returns:
        tuple: (lower, upper)
    """
    lower = base_value * (1 - percent_change)
    upper = base_value * (1 + percent_change)
    return lower, upper


def run_sensitivity():
    """
    This function will help run ±20% sensitivity analysis on all PK parameters.

    Args:
        None

    Returns:
        dict: simulation outputs for each parameter variation
    """
    results = {}

    for name, value in {
        "CL": CL,
        "VC": VC,
        "VP": VP,
        "Q": Q,
    }.items():

        low, high = vary_parameter(value)

        results[f"{name}_low"] = low
        results[f"{name}_high"] = high

    return results
