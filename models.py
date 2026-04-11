"""
models.py

This file serves as the core model for the pharmacokinetic ODE models used across all paper
reproductions.

What is included in these files:
1. A one-compartment baseline model
2. A two-compartment amiodarone model
"""

# ------------------------------------------------------------------------------------

# Importing in needed libraries
import numpy as np
from constants import CL, Vc, Vp, Q

# ------------------------------------------------------------------------------------


# The one-compartment baseline model
def first_compartment(t, C, CL, V):
    """
    The first compartment of the model for just one case.

    Args:
        t (float): time measured in hours
        C (float): the drug concentration in central compartment
        Cl (float): the clearance being measured
        V (float): the measured volume of the distribution

    Returns:
        The rate of of change of the concentration that we are measuring
    """
    return -(CL / V) * C


# ------------------------------------------------------------------------------------


# The two-compartment baseline model
def second_compartment(t, y, CL, Vc, Vp, Q):
    """
    The second comparment model for when there are two cases.

    Args:
        t (float): time measured in hours
        y (list): a list containing [Cc, Cp] with Cc = central compartment concentration
                  Cp = peripheral compartment concentration
        Cl (float): the clearance
        Vc (float): the measured central volume
        Vp (float): the measured perceptual volume
        Q (float): the inter-compartmental volume that is measured

    Returns:
        An array
    """
    Cc, Cp = y

    dCc_dt = -(CL / Vc) * Cc - (Q / Vc) * (Cc - Cp)
    dCp_dt = (Q / Vp) * (Cc - Cp)

    return [dCc_dt, dCp_dt]
