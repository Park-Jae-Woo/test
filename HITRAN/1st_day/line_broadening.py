import numpy as np
import matplotlib.pyplot as plt
from scipy.special import wofz

# X axis
x = np.linspace(-5, 5, 1000)

# print(x)

# Gaussian (Doppler)
sigma = 0.5
gaussian = np.exp(-x**2/(2*sigma**2)) / (sigma*np.sqrt(2*np.pi))

# Lorestzian (Pressure)
gamma = 0.5
lorentzian = gamma / (np.pi * (x**2 + gamma**2))

#print(lorentzian)

# Voigt profile
def voigt(x,sigma, gamma):
    z = (x + 1j*gamma) / (sigma*np.sqrt(2))
    return np.real(wofz(z)) / (sigma*np.sqrt(2*np.pi))

voigt_profile = voigt(x, sigma, gamma)
#print(voigt_profile)

plt.figure()
plt.plot(x, gaussian, label='Doppler (Gaussian)')
plt.plot(x, lorentzian, label='Pressure (Lorentzian)')
plt.plot(x, voigt_profile, label='Voigt Profile')
plt.legend()
plt.xlabel('Wavenumber offset')
plt.ylabel('Intensity')
plt.title('Line Broadening in FTIR')

plt.savefig("line_broadening.png", dpi=300)