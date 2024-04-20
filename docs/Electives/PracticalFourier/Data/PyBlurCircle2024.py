import numpy as np
import pylab
import matplotlib.pyplot as plt


# image size, square side length
ncols, nrows = 512, 512



image = np.zeros((nrows, ncols))
gmask = np.zeros((nrows, ncols))

cy, cx = nrows/2, ncols/2    

            

from skimage import data_dir           
from skimage.io import imread
image = imread(data_dir + "/brick.png")
            

orig_image = image            
pylab.imshow(image)
pylab.show()

# Take the 2-dimensional DFT and centre the frequencies
ftimage = np.fft.fft2(image)
ftimage = np.fft.fftshift(ftimage)
pylab.imshow(np.log(np.abs(ftimage)))
pylab.show()



sigmax, sigmay = 250, 250
#sigmax, sigmay = 25, 250

for ii in range(nrows):
    for jj in range(ncols): 
        RadSq=(((ii-cx)/sigmax)**2+((jj-cy)/sigmay)**2)
        if (RadSq**0.5 < 1):
            gmask[ii,jj] = 0.0*RadSq**0.1 +100
           


pylab.imshow(np.abs(gmask))
pylab.show()


ftimagep = ftimage * gmask
imagep = np.fft.ifft2(ftimagep)
pylab.imshow(np.abs(imagep))
pylab.show()
