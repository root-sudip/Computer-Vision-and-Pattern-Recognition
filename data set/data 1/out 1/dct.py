import sys, os
from PIL import Image
import numpy
import scipy.fftpack

# sourceImage = sys.argv[1]
sourceImage = 'denoised2.png'
image = Image.open('denoised2.png')
image = image.resize( (128,128), 1 )
#image = image.convert("L")

dctSize = image.size[0]

# get raw pixel values:
pixels = numpy.array(image.getdata(), dtype=numpy.float).reshape((dctSize, dctSize,3))

# perform 2-dimensional DCT (discrete cosine transform):
dct = scipy.fftpack.dct(scipy.fftpack.dct(pixels.T, norm="ortho").T, norm="ortho")

# create a series of images with increasingly larger parts of the DCT values being used:
os.mkdir("frames/")
for i in range(0, dctSize):
    dct2 = dct.copy()

    # zero out part of the higher frequencies of the DCT values:
    dct2[i:,:] = 0
    dct2[:,i:] = 0

    # perform 2d inverse DCT to get pixels back:
    idct = scipy.fftpack.idct(scipy.fftpack.idct(dct2.T, norm='ortho').T, norm='ortho')

    # clip/convert pixel values obtained by IDCT, and create image:
    # idct = idct.clip(0, 255)
    idct = idct.astype("uint8")
    
    img = Image.fromarray(idct)
    img = img.resize((512,512), Image.ANTIALIAS)
    #print img

    img.save("frames/img_%04d.png" % i)


os.system("convert -delay 30 -comment 'example of Discrete Cosine Transform (source image: %s)' frames/img_*.png dct.gif" % sourceImage)
