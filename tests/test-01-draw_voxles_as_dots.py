import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.append("..")
from learnsaxs import draw_voxles_as_dots

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
N = 10
canvas = np.ones((N,N,N))
draw_voxles_as_dots(ax, canvas)
plt.show()
