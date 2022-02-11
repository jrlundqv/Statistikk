import numpy as np

height_data = np.genfromtxt("height_data.csv", delimiter=",")


def find_median(data):
    data.sort()
    median_index = int(len(data) / 2)
    if (len(data) % 2) == 0:
        return (data[median_index] + data[median_index - 1]) / 2
    else:
        return data[median_index]


def find_mean_value(data):
    return sum(data) / len(data)


def find_variance(data):
    avg = find_mean_value(data)
    numerator = 0
    denominator = len(data) - 1
    for i in data:
        numerator += (i-avg)**2
    return numerator / denominator


def find_standard_deviation(data):
    return np.sqrt(find_variance(data))


print(f"Datapunktene er {height_data}")
print(f"a) Medianen er {find_median(height_data)}")
print(f"b) Middelverdien er {find_mean_value(height_data)}")
print(f"c) Variansen er {find_variance(height_data)}")
print(f"d) Standardavviket er {find_standard_deviation(height_data)}")
