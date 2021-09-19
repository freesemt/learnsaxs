import sys
import numpy as np
import matplotlib.pyplot as plt
sys.path.insert(0, "..")
from learnsaxs import draw_voxles_as_dots, get_detector_info, draw_detector_image

N = 32
canvas = np.zeros((N,N,N))
x = np.arange(N)
xx, yy, zz = np.meshgrid(x, x, x)

canvas[(xx - N/2)**2 + (yy - N/2)**2 + (zz - N/2)**2 < 4**2] = 1

fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(121, projection="3d")
ax2 = fig.add_subplot(122)

draw_voxles_as_dots(ax1, canvas)
F = np.fft.fftn(canvas)
q = np.linspace(0.005, 0.5, 80)
info = get_detector_info(q, F)
draw_detector_image(ax2, q, info.y)

fig.tight_layout()
plt.show()
