import numpy as np
import pylab

# image size, square side length, number of squares
ncols, nrows = 100, 100
circRad = 45

# The image array (0=background, 1=square) and boolean array of allowed places
# to add a square so that it doesn't touch another or the image sides
image = np.zeros((nrows, ncols))
gmask = np.zeros((nrows, ncols))
#sq_locs = np.zeros((nrows, ncols), dtype=bool)
#sq_locs[1:-sq_size-1,1:-sq_size-1] = True



# Add the required number of squares to the image
#for i in range(nsq):
#    place_square()
cy, cx = nrows/2, ncols/2    
for ii in range(nrows):
    for jj in range(ncols): 
        if (((ii-cx)**2+(jj-cy)**2)**0.5  < circRad ):
            image[ii,jj] = 100  
            



orig_image = image            
pylab.imshow(image)
pylab.show()

# Take the 2-dimensional DFT and centre the frequencies
ftimage = np.fft.fft2(image)
ftimage = np.fft.fftshift(ftimage)

pylab.imshow(np.log(np.abs(ftimage)))
pylab.show()


# Build and apply a Gaussian filter.
sigmax, sigmay = 12, 12

for ii in range(nrows):
    for jj in range(ncols): 
        RadSq=(((ii-cx)/sigmax)**2+((jj-cy)/sigmay)**2)
        if (RadSq**0.5 < 1):
            gmask[ii,jj] = 0*RadSq**0.1 + 25 
            #np.exp(-RadSq)  




pylab.imshow(np.abs(gmask))
pylab.show()



ftimagep = ftimage * gmask
#pylab.imshow(np.abs(ftimagep))
#pylab.show()


imagep = np.fft.ifft2(ftimagep)
pylab.imshow(np.abs(imagep))
pylab.show()
