"""
plotting.py

This file contains a method to create the benchmark plots for comparing simulated amiodarone
concentration-time curves to literature.
"""

# Importing in libraires
import matplotlib.pyplot as plt


# First model plotting just for One
def plot_first_comparemental_model(t, concentration):
    """
    This function will plot one-compartmental baseline curve.

    Args:
        t (array): simulation time points
        concentration (array): central concentration

    Returns:
        None
    """
    plt.figure(figsize=(8, 5))
    plt.plot(t, concentration, label="1-compartment")
    plt.xlabel("Time (hours)")
    plt.ylabel("Drug concentration")
    plt.title("One-Compartment Baseline")
    plt.grid(True)
    plt.legend()
    plt.show()


# Second model plotting for two
def plot_second_compartment(t, central, peripheral):
    """
    This function will plot main two-compartment benchmark curves.

    Args:
        t (array): simulation time points
        central (array): central compartment concentration
        peripheral (array): peripheral compartment concentration

    Returns:
        None
    """
    plt.figure(figsize=(8, 5))
    plt.plot(t, central, label="Central")
    plt.plot(t, peripheral, label="Peripheral")
    plt.xlabel("Time (hours)")
    plt.ylabel("Drug concentration")
    plt.title("Two-Compartment PK Model")
    plt.grid(True)
    plt.legend()
    plt.show()
