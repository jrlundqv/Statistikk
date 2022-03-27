import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress, t

katters_vekt = np.loadtxt("katters_vekt.csv", delimiter=",", usecols=2, skiprows=1)
hjertets_vekt = np.loadtxt("katters_vekt.csv", delimiter=",", usecols=3, skiprows=1)

plt.scatter(katters_vekt, hjertets_vekt)
plt.title("a) Spredeplott")
plt.xlabel("Kattens vekt i kg")
plt.ylabel("Hjertets vekt i gram")
plt.show()

beta, alfa, r, p, stderr = linregress(katters_vekt, hjertets_vekt)

print("b)")
print(f"Y = {alfa:.2f} + {beta:.2f}x")
print("Standardfeil for beta hatt =", round(stderr, 3))

plt.scatter(katters_vekt, hjertets_vekt)
plt.title("Spredeplott med regresjonslinje")
plt.xlabel("Kattens vekt i kg")
plt.ylabel("Hjertets vekt i gram")
plt.axline((0, alfa), slope=beta, color="r")
plt.xlim([1.905, 3.995])
plt.ylim([5.8, 21.2])
plt.show()

print("\nd)")
