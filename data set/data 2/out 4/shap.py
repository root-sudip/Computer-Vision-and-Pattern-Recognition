from PIL import Image
from PIL import ImageFilter

im = Image.open('denoised.png')
result = im.filter(ImageFilter.UnsharpMask)


result.save('abc m 2.png')