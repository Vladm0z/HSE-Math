#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 19:18:13 2022

@author: khokhlov
"""

import numpy as np
import matplotlib.pyplot as plt

from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rescale

from skimage.io import imread
from skimage import data_dir

#image = shepp_logan_phantom()
#image = imread(data_dir + "/camera.png")
#image = imread(data_dir + "/brick.png")

#image = imread(data_dir + "/logo.png",as_gray=True)
#image = imread(data_dir + "/gravel.png")
image = imread(data_dir + "/astronaut.png",as_gray=True)
#image = imread(data_dir + "/chessboard_GRAY.png")
#image = imread(data_dir + "/horse.png", as_gray=True)
image = rescale(image, scale=1.0, mode='reflect')
#, channel_axis=None)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.5))

ax1.set_title("Original")
ax1.imshow(image, cmap=plt.cm.Greys_r)

theta = np.linspace(0., 180., max(image.shape), endpoint=False)
sinogram = radon(image, theta=theta)
dx, dy = 0.5 * 180.0 / max(image.shape), 0.5 / sinogram.shape[0]
ax2.set_title("Radon transform\n(Sinogram)")
ax2.set_xlabel("Projection angle (deg)")
ax2.set_ylabel("Projection position (pixels)")
ax2.imshow(sinogram, cmap=plt.cm.Greys_r,
           extent=(-dx, 180.0 + dx, -dy, sinogram.shape[0] + dy),
           aspect='auto')

fig.tight_layout()
plt.show()