import matplotlib.pyplot as plt
import numpy as np
from hapi import *

db_begin('data')

###### Accessing Columns in a Table #######


nu1 = getColumn('H2O', 'nu')
nu, sw = getColumns('H2O', ['nu','sw'])
# nu: xaxis, location of i th spctral line
# sw: yaxis, strength of i th line

nu = np.array(nu)
sw = np.array(sw)

plt.figure(figsize=(10,4))

plt.vlines(nu, 0, sw)

plt.xlabel("Wavenumber (cm$^{-1}$)")
plt.ylabel("Line Intensity (cm/molecule)")
plt.title("H2O Line List (Stick Spectrum)")
plt.tight_layout()
plt.savefig("colums.png", dpi=300)