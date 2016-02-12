import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import scipy as sp
import scipy.interpolate as spi
import sys

gs = GridSpec(6, 3)
ax = plt.subplot(gs[1:5, 0])
ax1 = plt.subplot(gs[1:5, 1])
ax2 = plt.subplot(gs[1:5, 2])

x = [1, 2, 3, 4, 5, 6]
fx = [1, 3, 15, 12, 7, 3]
xs = np.linspace(.75, 6.25, 110)

# Piecewise Linear Interpolation
y = sp.interp(xs, x, fx)
ax.plot(x, fx, 'ro')
ax.plot(xs, y, label="Piecewise Linear Interpolant")
ax.set_xlabel('X Values')
ax.set_ylabel('Y Values')
ax.set_title("Piecewise Linear Interpolation")
ax.set_xlim([0, 7])
ax.set_ylim([-5, 20])
ax.grid(True)

# Lagrange polynomial interpolation
y1 = sp.interpolate.lagrange(x, fx)
y1 = y1(xs)
ax1.plot(x, fx, 'ro')
ax1.plot(xs, y1, label="Lagrange Polynomial Interpolant")
ax1.set_xlabel('X Values')
ax1.set_ylabel('Y Values')
ax1.set_title("Lagrange Polynomial Interpolation")
ax1.set_xlim([0, 7])
ax1.set_ylim([-5, 20])
ax1.grid(True)

# Spline Interpolation
yi = spi.splrep(x, fx, s=0)
y2 = spi.splev(xs, yi, der=0)
ax2.plot(x, fx, 'ro')
ax2.plot(xs, y2, label="Spline Interpolant")
ax2.set_xlabel('X Values')
ax2.set_ylabel('Y Values')
ax2.set_title("Spline Interpolation")
ax2.set_xlim([0, 7])
ax2.set_ylim([-5, 20])
ax2.grid(True)
plt.savefig("HW 2 Problem 3A Plot.png")
plt.show()
sys.exit()
