import matplotlib.pyplot as plt

import numpy as np

import scipy as sp
from scipy import ndimage
from scipy.misc import imfilter, imread
from scipy.signal import convolve2d as conv2
from scipy import ndimage as ndi
from scipy.misc import imsave

from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.feature_extraction.image import reconstruct_from_patches_2d
from sklearn.utils.fixes import sp_version
from sklearn.datasets import load_sample_image

from sklearn.decomposition import SparseCoder


from sklearn.decomposition import SparseCoder
from sklearn.decomposition import sparse_encode

from skimage import color
from skimage import io
from skimage import data, img_as_float
from skimage import feature

from PIL import Image

from os import listdir
from time import time


D = np.loadtxt('dic.txt',dtype=float)

t4 = time()

#noisy image input

while True:

	n_path = input('Enter noisy Image path : ')
	try:
		n0 = np.asarray(Image.open(n_path).resize((512,512), Image.ANTIALIAS))
	except FileNotFoundError:
		print('Entered wrong path : ')
	else:
		break

# n0 = n0 / 255

height, width, channel = n0.shape

# n0 = n0 + 0.075 * np.random.randn(height,width,3)

# n0 = n0 * 255

imsave('noisy.png',n0)

print('Enter patch size(X,Y) for extracting the patches for ')

n_width = int(input('X : '))
n_hight = int(input('Y : '))
n_patch_size = (n_width,n_hight)

n0_data = extract_patches_2d(n0,n_patch_size)

n0_data = n0_data.reshape(n0_data.shape[0], -1)

intercept = np.mean(n0_data, axis=0)
n0_data = n0_data - intercept

#need to update

# dico.set_params(transform_algorithm='omp',transform_n_nonzero_coefs = 1)
# code = dico.transform(n0_data)
# print('Code shape : ',code.shape)

#end

#start

coder = SparseCoder(dictionary=D, transform_n_nonzero_coefs=1,transform_alpha=3, transform_algorithm='omp')
code = coder.transform(n0_data)

#end

patches = np.dot(code,D)

print('Dot shape : ',patches.shape)

patches = patches + intercept

print('Patches shape : ',patches.shape)

patches = patches.reshape(n0_data.shape[0],n_patch_size[0],n_patch_size[1],3)

result =  reconstruct_from_patches_2d(patches,(height, width,3))

imsave('denoised.png',result)
print('Total time taken for sparse modeling : ',round((time()-t4),2))

#cython_lapack.cpython-34m.so
# cython_blas.cpython-34m.so

