import numpy as np

height_data = np.genfromtxt("height_data.csv", delimiter=",")

print(f"Median: {np.median(height_data)}")
print(f"Middelverdi: {np.mean(height_data)}")
print(f"Varians: {np.var(height_data, ddof=1)}")
print(f"Standardavvik: {np.std(height_data, ddof=1)}")
