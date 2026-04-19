"""
constants.py

This file stores all of the pharmacokinetic constants and simulation defaults used across
the the papers that we reading and benchmarking off of: Siddoway et al. (1996) and
Brodan et al. (1982) amiodarone papers.

Keeping these values centralized makes it easier to:
- reproduce published benchmark curves
- compare across both papers
- run sensitivity analysis
- keep units consistent
"""

# Published pharmacokinetic parameters based on the paper

CL = 0.22  # Clearance from central compartment (L/hr/kg)
Vc = 0.30  # Central compartment volume (L/kg)
Vp = 10.0  # Peripheral compartment volume L/kg
Q = 0.71  # Inter-compartmental clearance L/hr/kg

# --------------------------------------------------------------------------

# Simulation settings

TIME_START = 0  # Simulation start time (hours)
TIME_END = 200  # Simulation end time (hours)
NUM_POINTS = 200  # Number of output points in benchmark plots

# --------------------------------------------------------------------------

# Initial conditions

# Initial drug amount in central compartment
# Represents IV bolus dose used for benchmark reproduction
INITIAL_CENTRAL = 150

# Initial drug amount in peripheral compartment
INITIAL_PERIPHERAL = 0
