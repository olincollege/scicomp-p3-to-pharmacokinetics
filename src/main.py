"""
main.py

Main runner for SciComp Project 3:
reproducing amiodarone pharmacokinetic paper benchmarks.
"""

# Importing in Needed Libraries
from simulation import run_first_compartment, run_second_compartment
from plotting import plot_first_compartment, plot_second_compartment
from sensitivity import run_sensitivity


def main():
    """
    Run the full pharmacokinetic workflow.

    Includes:
    - baseline one-compartment model
    - primary two-compartment benchmark
    - sensitivity analysis
    """
    # =========================================================
    # 1) Baseline sanity check
    # =========================================================
    t1, c1 = run_first_compartment()
    plot_first_compartment(t1, c1)

    # =========================================================
    t2, central, peripheral = run_second_compartment()
    plot_second_compartment(t2, central, peripheral)

    # =========================================================
    # 3) Sensitivity analysis
    # =========================================================
    sensitivity_results = run_sensitivity()

    print("Sensitivity Results:")
    for key, value in sensitivity_results.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
