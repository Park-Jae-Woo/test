import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

opd = np.linspace(-1, 1, 4000)

# multi wave length
nu1 = 900
nu2 = 1000
nu3 = 1100

signal = (
    np.cos(2*np.pi*nu1*opd)
    + 0.7*np.cos(2*np.pi*nu2*opd)
    + 0.5*np.cos(2*np.pi*nu3*opd)
)

plt.figure(figsize=(8,4))
plt.plot(opd, signal)
plt.xlabel("Optical Path Difference (cm)")
plt.ylabel("Signal")
plt.title("Multi-Wavenumber Interferogram")
plt.tight_layout()
plt.savefig("multi_interferogram.png", dpi=300)

print("We draw this figure")