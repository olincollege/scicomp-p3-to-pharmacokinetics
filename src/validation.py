"""
validation.py

Validation metrics for comparing simulated pharmacokinetic
curves against published paper benchmark data.
"""

import numpy as np


def rmse(simulated, observed):
    """
    Computing the root mean squared error. This will measure how closely the simulated
    concentration-time curve matches the paper.

    Args:
        simulated (array): model output
        observed (array): published paper values

    Returns:
        float: RMSE score
    """
    simulated = np.array(simulated)
    observed = np.array(observed)

    return np.sqrt(np.mean((simulated - observed) ** 2))


def percent_error(simulated, observed):
    """
    Computes the average percent error. This will help for reporting model agreement in a
    way that is easier to interpret than RMSE alone.

    Args:
        simulated (array): model output
        observed (array): paper benchmark values

    Returns:
        float: average percent error
    """
    simulated = np.array(simulated)
    observed = np.array(observed)

    return np.mean(np.abs((observed - simulated) / observed)) * 100
