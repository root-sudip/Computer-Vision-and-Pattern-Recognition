import matplotlib.pyplot as plt

import numpy as np

import scipy as sp
from scipy import ndimage
from scipy.misc import imfilter, imread
from scipy.signal import convolve2d as conv2
from scipy import ndimage as ndi
from scipy.misc import imsave


from sklearn.decomposition import DictionaryLearning
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

from PIL import ImageFilter


print('Enter the Patch size(X,Y) for making the Dictionary : ')

p_width = int(input('X : '))
p_hight = int(input('Y : '))


patch_size = (p_width,p_hight)

reshape_size = (512,512)

while True:
	i_path = input('Initial Image Path : ')
	try:
		initial = np.asarray(Image.open(i_path).resize(reshape_size, Image.ANTIALIAS))
	except FileNotFoundError:
		print('Entered wrong path ')
	else:
		break

data = extract_patches_2d(initial,patch_size)

total_img = 0

total_images = int(input('Enter total Images : '))

while True:
	path = input('Path for source of the Images : ')
	try:
		for f in listdir(path):
			if f.endswith('.jpg'):
				if(total_img <= total_images):
					total_img = total_img + 1
					print(f)
					print('Data shape : ',data.shape)
					print('Total file : ',total_img)

					A = np.asarray(Image.open(path+f).resize(reshape_size, Image.ANTIALIAS))
					X =  extract_patches_2d(A,patch_size)
					data = np.append(data,X,axis=0)
					print('patch shape',X.shape)
				else:
					break
	except FileNotFoundError:
		print('Entered wrong path :')
	else:
		break

print('Total number of Image : ',total_img)
print('Total Patches : ',data.shape)
print('Total size of the array : ',data.nbytes)

t0 = time()
 
data = data.reshape(data.shape[0],-1)
print('Extracted patches shape : ',data.shape)


data = data - np.mean(data,axis=0)
data = data / np.std(data, axis=0)

t1 = time()
print('Total time taken to extract patches : ',round((t1-t0),2),' sec')


t2 = time()
n_iter = int(input('Enter number of interations for Dictionary Learning : '))

print('Learning the Dictionary ....')

dico =  MiniBatchDictionaryLearning(n_components=100,alpha=3,n_iter=n_iter)

V = dico.fit(data).components_
print('Dic shape : ',V.shape)
t3 = time()
print('No of iteration : ',n_iter)
print('Total time taken for Dictionary learning : ',round((t3-t2),2),' sec')



filename = input('Enter File Name to store Dictionary : ')
np.savetxt(filename,V,fmt="%f")
