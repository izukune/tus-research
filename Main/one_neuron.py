import numpy as np
import matplotlib.pyplot as plt

X = np.arange(-1.0, 1.0, 0.2)
Y = np.arange(-1.0, 1.0, 0.2)

Z = np.zeros((10,10))

w_X = 2.5
w_Y = 3.0

bias = 0.1

for i in range(10):
    for j in range(10):
        u = X[i] * w_X + Y[j] * w_Y + bias

        y = 1/(1 + np.exp(-u))

        Z[j][i] = y

plt.imshow(Z, "gray", vmin = 0.0, vmax=1.0)
plt.colorbar()
plt.show()