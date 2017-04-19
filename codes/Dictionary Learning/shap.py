from PIL import Image
from PIL import ImageFilter

im = Image.open('denoised.png')
result = im.filter(ImageFilter.UnsharpMask)
#result = result.filter(ImageFilter.UnsharpMask)

result.save('s-024.png')