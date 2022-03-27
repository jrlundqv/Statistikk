from scipy.stats import pearsonr
import numpy as np

katters_vekt = np.loadtxt("katters_vekt.csv", delimiter=",", usecols=2, skiprows=1)
hjertets_vekt = np.loadtxt("katters_vekt.csv", delimiter=",", usecols=3, skiprows=1)

r, p = pearsonr(katters_vekt, hjertets_vekt)

print("r =", r)
