from scipy.stats import t

p = 1 - t.cdf(3.53, 9)

print("p =", p)
