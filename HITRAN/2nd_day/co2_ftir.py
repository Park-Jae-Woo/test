import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt
from hapi import *

# data
db_begin('CO2_data')

# constant
T = 296.0   # Temperature (K)
p = 1.0     # Pressure (atm)
L = 10.0    # Path length (cm)

# Voigt profile
nu, coef = absorptionCoefficient_Voigt(
    SourceTables='CO2',
    HITRAN_units=False,
    Environment={'T': T, 'p': p},
    WavenumberRange=[2200, 2400],
    WavenumberStep=0.01
)

# Beer-Lambert law process
transmittance = np.exp(-coef * L)

# figure
plt.figure(figsize=(8,4))
plt.plot(nu, transmittance)
plt.xlabel("Wavenumber (cm$^{-1}$)")
plt.ylabel("Transmittance")
plt.title("CO2 Spectrum (4.3 μm band)")
plt.tight_layout()
plt.savefig("co2_ftir.png", dpi=300)

print("we draw this figure")