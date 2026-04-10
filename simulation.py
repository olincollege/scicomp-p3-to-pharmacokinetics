"""
simulation.py

This file will help us run the pharmacokinetic simulations using ODE models
"""

# Importing in needed libraries
import numpy as np
from scipy.integrate import solve_ivp
from constants import (
    TIME_START,
    TIME_END,
    NUM_POINTS,
    INITIAL_CENTRAL,
    INITIAL_PERIPHERAL,
    CL,
    Vc,
    Vp,
    Q,
)
from models import first_compartment, second_compartment


# Using the one-compartmental model to go through the simulation
def run_first_compartment():
    """
    This file will run the single compartment baseline simulation

    Args:
        None

    Returns:
        A tuple with the timeppoints and concentration values
    """
    t_eval = np.linspace(TIME_START, TIME_END, NUM_POINTS)

    solution = solve_ivp(
        first_compartment,
        [TIME_START, TIME_END],
        [INITIAL_CENTRAL],
        args=(CL, VC),
        t_eval=t_eval,
    )

    return solution.t, solution.y[0]
