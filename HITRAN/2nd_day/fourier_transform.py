import matplotlib
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Optical Path Difference 
# -----------------------------
opd_max = 1.0          
N = 4096               
opd = np.linspace(-opd_max, opd_max, N)

# -----------------------------
# 2. Spectrum (3 line)
# -----------------------------
nu1 = 900
nu2 = 1000
nu3 = 1100

interferogram = (
    np.cos(2*np.pi*nu1*opd)
    + 0.7*np.cos(2*np.pi*nu2*opd)
    + 0.5*np.cos(2*np.pi*nu3*opd)
)

# -----------------------------
# 3. Run Fourier Transform
# -----------------------------
spectrum = np.fft.fftshift(np.fft.fft(interferogram))
freq = np.fft.fftshift(np.fft.fftfreq(N, d=(opd[1]-opd[0])))

intensity = np.abs(spectrum)

# -----------------------------
# 4. figure
# -----------------------------
plt.figure(figsize=(8,4))
plt.plot(freq, intensity)
plt.xlim(800, 1200)
plt.xlabel("Wavenumber (cm$^{-1}$)")
plt.ylabel("Intensity")
plt.title("Recovered Spectrum from Interferogram")
plt.tight_layout()
plt.savefig("ft.png", dpi=300)

print("We draw this figure")