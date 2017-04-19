from PIL import Image
from scipy.misc import imfilter, imread, imsave
import numpy as np

img = np.asarray(Image.open('r-024.png').resize((300,300), Image.ANTIALIAS))

imsave('r-046-2.png',img)
