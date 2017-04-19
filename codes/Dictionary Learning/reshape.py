from PIL import Image
from scipy.misc import imfilter, imread, imsave
import numpy as np

img = np.asarray(Image.open('024.jpg').resize((512,512), Image.ANTIALIAS))

imsave('r-024.png',img)