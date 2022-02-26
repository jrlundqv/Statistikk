import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

print("** Binomisk forsøksrekke **")
n = int(input("Antall forsøk n: "))
p = float(input("Sannsynligheten p: "))

x_values = np.arange(n + 1)

plot1 = plt.figure(1)
plt.title("Punktsannsynlighet P(X=x)")
plt.bar(x_values, binom.pmf(x_values, n, p))

plot2 = plt.figure(2)
plt.title("Kumulativ sannsynlighet P(X≤x)")
plt.bar(x_values, binom.cdf(x_values, n, p))

print("\nPunktsannsynlighet P(X=x)")
for x in x_values:
    point_probability = binom.pmf(x, n, p)
    if point_probability < 0.0005:
        if point_probability > binom.pmf(x+1, n, p):
            if x == n:
                print(f"P(X={x}) = {point_probability:.3f}")
            else:
                print(f"∀x ≥ {x} P(X=x) = {point_probability:.3f}")
                break
        elif binom.pmf(x+1, n, p) >= 0.0005:
            if x == 0:
                print(f"P(X={x}) = {point_probability:.3f}")
            else:
                print(f"∀x ≤ {x} P(X=x) = {point_probability:.3f}")
        elif point_probability < binom.pmf(x+1, n, p):
            continue
    else:
        print(f"P(X={x}) = {point_probability:.3f}")

print("\nKumulativ sannsynlighet P(X≤x)")
for x in x_values:
    cumulative_probability = binom.cdf(x, n, p)
    if 0.9995 >= cumulative_probability >= 0.0005:
        print(f"P(X≤{x}) = {cumulative_probability:.3f}")
    elif cumulative_probability < 0.0005:
        if binom.cdf(x+1, n, p) < 0.0005:
            continue
        else:
            print(f"P(X≤{x}) = {cumulative_probability:.3f}")
    else:
        if x == x_values[-1]:
            print(f"P(X≤{x}) = {binom.cdf(x, n, p):.0f}")
        else:
            print(f"P(X≤{x}) = {cumulative_probability:.3f}")
            print(f"P(X≤{x_values[-1]}) = {binom.cdf(x_values[-1], n, p):.0f}")
            break

plt.show()
