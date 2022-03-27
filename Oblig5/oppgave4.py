import scipy.stats as stats
import numpy as np

alfa = float(input("Signifikansnivå \u03b1: "))
my_0 = float(input("Forventningsverdi \u03bc\u2080: "))

print("a)")
print("H\u2080: Vekten til kattene er den samme på slutten av turistsesongen som ellers i året \u03bc \u2264 "
      "\u03bc\u2080 =", my_0)
print("H\u2081: Vekten til kattene er høyere på slutten av turistsesongen enn ellers i året \u03bc > \u03bc\u2080 =",
      my_0)

katters_vekt = np.loadtxt("katters_vekt.csv", delimiter=",", usecols=2, skiprows=1)
x_mean = np.mean(katters_vekt)

print("\nb)")
print("x̄ =", round(x_mean, 3))
n = katters_vekt.size

t, p_verdi = stats.ttest_1samp(katters_vekt, my_0, alternative="greater")
print("t =", round(t, 3))

t_alpha = stats.t.ppf(1 - alfa, n - 1)
print("t\u2090 =", round(t_alpha, 3))

if t > t_alpha:
    print(f"\nt = {round(t, 3)} > t\u2090 = {round(t_alpha, 3)}")
    print("Vi forkaster H\u2080 på signifikansnivå \u03b1 =", alfa)
elif t <= t_alpha:
    print(f"\nt = {round(t, 3)} < t\u2090 = {round(t_alpha, 3)}")
    print("Vi beholder H\u2080 på signifikansnivå \u03b1 =", alfa)
else:
    print("Verdifeil. Resultat ikke gyldig.")

print("\nc)")
print("p =", round(p_verdi, 3))

print("\nd)")
print("Signifikansnivået som er grensen mellom å beholde H\u2080 og å forkaste H\u2080 er \u03b1 =", p_verdi)

print("\ne)")
print("Verdien for \u03bc\u2080 som er grensen mellom å forkaste og beholde H\u2080 er ca. 2.82117")
