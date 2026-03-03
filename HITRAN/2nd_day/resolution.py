import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------
# parameter
# ----------------------------
delta_opd = 0.0005
opd_full = np.arange(-2.0, 2.0, delta_opd)

nu1 = 1000
nu2 = 1005

# full interferogram
interferogram_full = (
    np.cos(2*np.pi*nu1*opd_full)
    + np.cos(2*np.pi*nu2*opd_full)
)

# ----------------------------
# OPD 2.0 (Full)
# ----------------------------
spec_h = np.fft.fftshift(np.fft.fft(interferogram_full))
freq = np.fft.fftshift(np.fft.fftfreq(len(opd_full), d=delta_opd))

# ----------------------------
# OPD 0.2 (Cut)
# ----------------------------
mask = np.abs(opd_full) <= 0.2
interferogram_cut = interferogram_full * mask

spec_l = np.fft.fftshift(np.fft.fft(interferogram_cut))

# ----------------------------
# Plot
# ----------------------------
plt.figure(figsize=(8,4))

plt.plot(freq, np.abs(spec_h),
         color='blue', label='OPD 2.0 cm')

plt.plot(freq, np.abs(spec_l),
         color='orange', label='OPD 0.2 cm')

plt.xlim(980, 1025)
plt.xlabel("Wavenumber (cm$^{-1}$)")
plt.ylabel("Intensity")
plt.legend()
plt.tight_layout()

plt.savefig("resolution_compare.png", dpi=300)

print("We draw this figure")
