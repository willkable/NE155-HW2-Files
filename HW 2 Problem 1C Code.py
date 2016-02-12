import numpy as np
import matplotlib.pyplot as plt
import sys

plt.show()
x = np.arange(-.5, 4.5, 0.05)
original = (np.cos(np.pi / 2 * x)) + (x ** 2) / 2
interpolant = (-x ** 3 / 6) + 2 * x ** 2 - 10 * x / 3 + 1

plt.plot([0, 2, 3, 4], [1, 1, 4.5, 9], 'ro')
plt.plot(x, original, label="Original")
plt.plot(x, interpolant, label="Interpolant")
plt.draw()
plt.legend(loc="lower right")
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Original Function vs. Interpolant')
plt.grid(True)
plt.savefig("HW 2 Problem 1C Plot.png")
plt.show()
sys.exit()
