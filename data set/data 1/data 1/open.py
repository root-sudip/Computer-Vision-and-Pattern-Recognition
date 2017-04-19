from PIL import Image
import numpy as np
from os import listdir
from sklearn.feature_extraction.image import extract_patches_2d


data = np.array([]).reshape((0,8,8))

# for f in listdir('.'):
# 	A = np.asarray(Image.open(f).resize((512,512), Image.ANTIALIAS))
# 	X =  extract_patches_2d(c,(8,8))
# 	data = np.append(data,X,axis=0)

# print(data.shape)
A = np.asarray(Image.open('009.jpg').resize((512,512), Image.ANTIALIAS))
X =  extract_patches_2d(A,(8,8))
print(X.shape)


from PIL import Image
import numpy as np
from os import listdir
from sklearn.feature_extraction.image import extract_patches_2d


data = np.array([]).reshape((0,8,8,3))

for f in listdir('.'):
        if f.endswith('.jpg'):
                A = np.asarray(Image.open(f).resize((512,512), Image.ANTIALIAS))
                X =  extract_patches_2d(A,(8,8))
                data = np.append(data,X,axis=0)

print(data.shape)
~                   
