from PIL import Image
from PIL import ImageFilter

im = Image.open('denoised m-2.png')
result = im.filter(ImageFilter.UnsharpMask)
result = result.filter(ImageFilter.UnsharpMask)

result.save('abc 61.png')