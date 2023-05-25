import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def gaussian(x, y, mu_x, mu_y, sigma_x, sigma_y):
    return np.exp(-0.5 * ((x - mu_x) ** 2 / sigma_x ** 2 + (y - mu_y) ** 2 / sigma_y ** 2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.linspace(-3, 3, 200)
Y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(X, Y)
Z = gaussian(X, Y, 0, 0, 1, 1)

ax.plot_surface(X, Y, Z, cmap='coolwarm')

plt.show()
