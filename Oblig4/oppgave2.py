from statsmodels.graphics.gofplots import qqplot
import numpy as np
import matplotlib.pyplot as plt

weight_data = np.genfromtxt("katters_vekt.csv", skip_header=1, delimiter=",", usecols=(2,))
heart_data = np.genfromtxt("katters_vekt.csv", skip_header=1, delimiter=",", usecols=(3,))

qqplot(weight_data, line="s")
plt.title("Bodyweight")
plt.show()

qqplot(heart_data, line="s")
plt.title("Heart weight")
plt.show()
