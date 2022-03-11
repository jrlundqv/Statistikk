import random
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

dice_throws = int(input("Hvor mange kast per omgang? "))
rounds = int(input("Hvor mange omganger? "))
value_list = []

x_values = np.arange(1, rounds+1)

for i in range(rounds):
    dice_sum = 0
    for j in range(dice_throws):
        dice = random.randint(1, 6)
        dice_sum += dice

    dice_avg = dice_sum / dice_throws
    value_list.append(dice_avg)

print(f"Totalt gjennomsnitt: {sum(value_list) / rounds:.3f}")
print(f"Utvalgsstandardavvik: {np.std(value_list):.3f}")
print(f"Teoretisk standardavvik: {1.708/np.sqrt(dice_throws):.3f}")

value_array = np.array(value_list)
qqplot(value_array, line="s")
plt.title(f"{dice_throws} kast per omgang\n {rounds} omganger")
plt.show()

plt.hist(value_list, bins=30, rwidth=0.85)
plt.title(f"Fordeling av snittverdien til terning ved\n{dice_throws} kast per omgang og totalt {rounds} omganger")
plt.xlabel("Snittverdi per omgang")
plt.ylabel("Forekomster av snittverdi")
plt.show()
