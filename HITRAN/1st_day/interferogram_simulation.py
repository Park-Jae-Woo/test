import numpy as np
import matplotlib.pyplot as plt

# OPD
opd = np.linspace(-2, 2, 1000)

# Wave Number
wavenumber = 10  # arbitrary
interferogram = np.cos(2*np.pi*wavenumber*opd)

plt.figure()
plt.plot(opd, interferogram)
plt.xlabel("Optical Path Difference")
plt.ylabel("Signal")
plt.title("Simulated FTIR Interferogram")
plt.savefig("interferogram.png", dpi=300)