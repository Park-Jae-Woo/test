import numpy as np
import matplotlib.pyplot as plt

opd = np.linspace(-2, 2, 2048)
wavenumber = 10
interferogram = np.cos(2*np.pi*wavenumber*opd)

# Fourier Transform
spectrum = np.fft.fftshift(np.fft.fft(interferogram))
freq = np.fft.fftshift(np.fft.fftfreq(len(opd), d=opd[1]-opd[0]))

plt.figure()
plt.plot(freq, np.abs(spectrum))
plt.xlabel("Wavenumber")
plt.ylabel("Intensity")
plt.title("Recovered Spectrum from Interferogram")
plt.savefig("fourier_transform.png", dpi=300)