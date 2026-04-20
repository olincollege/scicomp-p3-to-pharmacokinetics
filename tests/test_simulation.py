"""
test_simulation.py

Tests for numerical simulation outputs.
Ensures solver behavior and physical constraints are valid.
"""

from simulation import run_first_compartment, run_second_compartment


def test_time_increasing():
    """
    Ensure that time values returned by the solver are strictly increasing.
    This verifies correct time integration.
    """
    t, _ = run_first_compartment()

    # Each time step should be larger than the previous one
    assert all(t[i] < t[i + 1] for i in range(len(t) - 1))


def test_non_negative_concentrations():
    """
    Concentrations should never be negative.
    Negative values would be physically impossible.
    """
    _, central, peripheral = run_second_compartment()

    assert all(c >= 0 for c in central)
    assert all(p >= 0 for p in peripheral)


def test_initial_conditions():
    """
    Verify that simulation starts with correct initial values:
    - central compartment contains drug
    - peripheral compartment starts at zero
    """
    _, central, peripheral = run_second_compartment()

    assert central[0] > 0
    assert peripheral[0] == 0


def test_total_concentration_decreases():
    """
    Total drug amount should decrease over time due to clearance.

    This is a key pharmacokinetic property:
    the body eliminates drug rather than creating it.
    """
    _, central, peripheral = run_second_compartment()

    # Approximate total drug (sum of compartments)
    total = [c + p for c, p in zip(central, peripheral)]

    # Final amount should be less than initial
    assert total[-1] < total[0]
