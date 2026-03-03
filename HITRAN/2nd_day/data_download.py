from hapi import *

db_begin('CO2_data')

fetch('CO2', 2, 1, 2200, 2400)
print("CO2 data download complete")