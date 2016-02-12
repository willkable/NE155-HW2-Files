import numpy as np
import matplotlib.pyplot as plt
import sys

H = [5.00000e-02, 2.50000e-02, 1.25000e-02, 6.25000e-03, 3.12500e-03, 1.56250e-03, 7.81250e-04, 3.90625e-04]
E = [1.036126e-01, 3.333834e-02, 1.375409e-02, 4.177237e-03, 1.103962e-03, 2.824698e-04, 7.185644e-05, 1.813937e-05]
# this is where I did all my calculations 4C
Hlog = np.log10(H)
Hlog2 = (np.log10(H) ** 2)
SumH = sum(Hlog)
SumH2 = sum(Hlog2)
Elog = np.log10(E)
SumE = sum(Elog)
SumEH = sum(Elog * Hlog)

# This is where I did my plot for 4D
xs = np.linspace(0, .06, 100)
y = 28.2227 * xs ** 1.7891
plt.loglog(H, E, "ro", label="Original Data")
plt.loglog(xs, y, label='Least Squares Estimate')
plt.draw()
plt.legend(loc="lower right")
plt.xlabel('log(H)')
plt.ylabel('log(E)')
plt.title('Original Function vs. Least Squares Estimate')
plt.grid(True)
plt.savefig("HW 2 Problem 4D Plot.png")
plt.show()
sys.exit()
