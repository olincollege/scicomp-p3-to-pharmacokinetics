"""
test_models.py

Unit tests that are used for the pharmacokinetic ODE models.
These tests verify mathematical behavior and physical realism.
"""

# Importing in Libraries needed
from models import first_compartment, second_compartment


def test_first_compartment_decay():
    """
    Test that the one-compartment model produces a negative derivative
    when the amount is positive (drug should be eliminated over time).
    """
    dA = first_compartment(0, [10], CL=0.2, V=1.0)

    # Expect decay to derivative must be negative
    assert dA[0] < 0


def test_second_compartment_returns_two_values():
    """
    Test that the two-compartment model returns two derivatives:
    one for the central compartment and one for the peripheral compartment.
    """
    dA = second_compartment(0, [10, 0], CL=0.2, Vc=1.0, Vp=2.0, Q=0.5)

    # Should return [dAc/dt, dAp/dt]
    assert len(dA) == 2


def test_mass_transfer_direction():
    """
    Test that drug initially moves from central to peripheral compartment.

    At t=0:
    - central compartment should decrease
    - peripheral compartment should increase
    """
    dAc, dAp = second_compartment(0, [10, 0], CL=0.2, Vc=1.0, Vp=2.0, Q=0.5)

    # Central loses drug
    assert dAc < 0

    # Peripheral gains drug
    assert dAp > 0
