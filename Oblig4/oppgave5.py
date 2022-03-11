from scipy.stats import norm
import numpy as np

n = int(input("Utvalgets størrelse: "))
x = int(input("Antall gunstige utfall blant utvalget: "))
KI_percent = int(input("Ønsket konfidensintervall i %: "))
KI = KI_percent / 100
p = x / n

if n * p * (1 - p) >= 5:
    print("Variansen er større enn eller lik 5 og x er tilnærmet normalfordelt")
else:
    print("Variansen er mindre enn 5 og x oppfyller ikke kravet for å være tilnærmet normalfordelt")

interval = (norm.ppf((1-KI)/2) * -1) * np.sqrt((p * (1-p)) / n)

interval_array = [round(p - interval, 3), round(p + interval, 3)]

print(f"Et {KI_percent}% konfidensintervall for p er:")
print(interval_array)
