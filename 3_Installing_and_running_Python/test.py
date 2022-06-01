import numpy as np
import matplotlib.pyplot as plt

print("Hello World!")

x = np.linspace(-10,10,1000)

plt.plot(x, np.cos(x))
plt.title("Good Job!")
plt.show()
