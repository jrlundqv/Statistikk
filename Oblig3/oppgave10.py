import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x_range = np.arange(720, 800)
my = 760
sigma = 10

plt.plot(x_range, norm.pdf(x_range, my, sigma))
plt.title("Normalfordeling")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()

x = int(input("Hvilken x verdi ønsker du å regne ut F(x) for? "))
print(f"P(X≤{x}) = {norm.cdf(x, my, sigma):.3f}")
