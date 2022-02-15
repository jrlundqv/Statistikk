import numpy
import matplotlib.pyplot as pyplot
import scipy.stats as stats

print("** Binomisk forsøksrekke **")
n = int(input("Antall forsøk n: "))
p = float(input("Sannsynligheten p: "))

x_values = numpy.arange(n + 1)

plot1 = pyplot.figure(1)
pyplot.title("Punktsannsynlighet P(X=x)")
pyplot.bar(x_values, stats.binom.pmf(x_values, n, p))

plot2 = pyplot.figure(2)
pyplot.title("Kumulativ sannsynlighet P(X≤x)")
pyplot.bar(x_values, stats.binom.cdf(x_values, n, p))

print("\nPunktsannsynlighet P(X=x)")
for x in x_values:
    point_probability = stats.binom.pmf(x, n, p)
    if point_probability < 0.0005:
        if point_probability > stats.binom.pmf(x+1, n, p):
            if x == n:
                print(f"P(X={x}) = {point_probability:.3f}")
            else:
                print(f"∀x ≥ {x} P(X=x) = {point_probability:.3f}")
                break
        elif stats.binom.pmf(x+1, n, p) >= 0.0005:
            if x == 0:
                print(f"P(X={x}) = {point_probability:.3f}")
            else:
                print(f"∀x ≤ {x} P(X=x) = {point_probability:.3f}")
        elif point_probability < stats.binom.pmf(x+1, n, p):
            continue
    else:
        print(f"P(X={x}) = {point_probability:.3f}")

print("\nKumulativ sannsynlighet P(X≤x)")
for x in x_values:
    cumulative_probability = stats.binom.cdf(x, n, p)
    if 0.9995 >= cumulative_probability >= 0.0005:
        print(f"P(X≤{x}) = {cumulative_probability:.3f}")
    elif cumulative_probability < 0.0005:
        if stats.binom.cdf(x+1, n, p) < 0.0005:
            continue
        else:
            print(f"P(X≤{x}) = {cumulative_probability:.3f}")
    else:
        print(f"P(X≤{x}) = {cumulative_probability:.3f}")
        print(f"P(X≤{x_values[-1]}) = {stats.binom.cdf(x_values[-1], n, p):.0f}")
        break

pyplot.show()
