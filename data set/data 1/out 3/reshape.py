from PIL import Image
from scipy.misc import imfilter, imread, imsave
import numpy as np

img = np.asarray(Image.open('039.jpg').resize((512,512), Image.ANTIALIAS))

imsave('039.png',img)