from scipy.stats import chi2
import numpy as np

data = np.loadtxt("salmonella_data.csv", delimiter=",")
n = len(data)
KI = [0.9, 0.92, 0.95, 0.99]
interval = []

print("Punktestimat")
sigma2 = 1/(n-1) * ((sum(data**2)) - (n * np.mean(data)**2))
sigma = np.sqrt(sigma2)
print(f"\u03C3\u0302 = {sigma:.1f}")

print("\nKonfidensintervall")
for alfa in KI:
    bottom_interval = np.sqrt(((n-1) * sigma2) / chi2.ppf(((1 - alfa)/2) + alfa, n - 1))
    top_interval = np.sqrt(((n-1) * sigma2) / chi2.ppf((1 - alfa)/2, n - 1))
    interval.append(round(bottom_interval, 1))
    interval.append(round(top_interval, 1))
    print(f"Et {alfa * 100:.0f}% konfidensintervall for \u03C3: {interval}")
    interval.clear()
