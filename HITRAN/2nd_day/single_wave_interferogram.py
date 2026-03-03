import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

# OPD(Optical Path Difference) [cm]
opd = np.linspace(-1, 1, 2000)

# single nu (cm^-1)
nu = 1000

# Interferogram
signal = np.cos(2 * np.pi * nu * opd)

plt.figure(figsize=(8,4))
plt.plot(opd, signal)
plt.xlabel("Optical Path Difference (cm)")
plt.ylabel("Signal")
plt.title("Single Wavenumber Interferogram")
plt.tight_layout()
plt.savefig("single_interferogram.png", dpi=300)

print("We daraw this figure")