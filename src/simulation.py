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
        A tuple with the time points and concentration values
    """
    t_eval = np.linspace(TIME_START, TIME_END, NUM_POINTS)

    solution = solve_ivp(
        first_compartment,
        [TIME_START, TIME_END],
        [INITIAL_CENTRAL],
        args=(CL, Vc),
        t_eval=t_eval,
    )

    return solution.t, solution.y[0]


def run_second_compartment():
    """
    The goal is to run the main two-compartment benchmark simulation. This essentially is the main
    simulation code function that will be used to reproduce the published plasma concentration-time
    curves.

    Args:
        None

    Returns:
        A tuple containing the time points, central concentration, peripheral concentration
    """
    t_eval = np.linspace(TIME_START, TIME_END, NUM_POINTS)

    solution = solve_ivp(
        second_compartment,
        [TIME_START, TIME_END],
        [INITIAL_CENTRAL, INITIAL_PERIPHERAL],
        args=(CL, Vc, Vp, Q),
        t_eval=t_eval,
    )

    central = solution.y[0]
    peripheral = solution.y[1]

    return solution.t, central, peripheral
