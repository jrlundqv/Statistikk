import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

print("Poisson-fordeling X~poisson(λt)")
lambdat = float(input("Parameter λt: "))
x_upper_limit = int(input("Øvre grense for X: "))

x_values = np.arange(x_upper_limit + 1)

for x in x_values:
    poisson_probability = poisson.pmf(x, lambdat)
    if poisson_probability >= 0.0005:
        print(f"P(X={x}) = {poisson_probability:.3f}")

plt.bar(x_values, poisson.pmf(x_values, lambdat))
plt.show()
