import numpy as np
import matplotlib.pyplot as plt
import sys

plt.show()
x = np.arange(-.5, 4.5, 0.05)
original = (np.cos(np.pi / 2 * x)) + (x ** 2) / 2
interpolant = (.0813*x ** 3) + .42678 * x ** 2 - 1.0079 * x + 1
xset = [0.0, 1.0, 2.5, 4.0]
ox = np.ones(len(xset))
for i in range(len(xset)):
    ox[i] = (np.cos(np.pi / 2 * xset[i])) + (xset[i] ** 2) / 2


plt.plot(xset, ox, 'ro')
plt.plot(x, original, label="Original")
plt.plot(x, interpolant, label="Interpolant")
plt.draw()
plt.legend(loc="lower right")
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('Original Function vs. Interpolant')
plt.grid(True)
plt.ylim([-2, 12])
plt.savefig("HW 2 Problem 1D Plot.png")
plt.show()
sys.exit()
