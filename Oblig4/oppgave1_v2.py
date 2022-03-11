import random
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.gofplots import qqplot

dice_throws = int(input("Hvor mange kast per omgang? "))
rounds = int(input("Hvor mange omganger? "))
value_list = [0] * 30
avg_list = []

x_values = np.arange(1, 6.1, 5 / 29)

for i in range(rounds):
    dice_sum = 0
    for j in range(dice_throws):
        dice = random.randint(1, 6)
        dice_sum += dice
    dice_avg = dice_sum / dice_throws
    avg_list.append(dice_avg)

    x = 0
    while x < 30:
        if dice_avg - x_values[x] < (5 / 29)/2 and x_values[x] - dice_avg < (5 / 29)/2:
            index_value = value_list.pop(x)
            index_value += 1
            value_list.insert(x, index_value)
            break
        x += 1

avg_array = np.array(avg_list)
qqplot(avg_array, line="s")
plt.title(f"{dice_throws} kast per omgang\n {rounds} omganger")
plt.show()

plt.bar(x_values, value_list, width=0.15)
plt.title(f"Fordeling av snittverdien til terning ved\n{dice_throws} kast per omgang og totalt {rounds} omganger")
plt.xlabel("Snittverdi per omgang")
plt.ylabel("Forekomster av snittverdi")
plt.show()
