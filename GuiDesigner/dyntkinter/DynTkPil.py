from PIL.Image import *
from PIL.Image import open as image_open
 
from PIL.ImageTk import BitmapImage as BitmapImage
from PIL.ImageTk import PhotoImage as imagetk_photoimage
 
 
def open(filename,mode='r'):
    image = image_open(filename,mode)
    image.filename = filename
    return image
 
   
def PhotoImage(pil_image):
    image = imagetk_photoimage(pil_image)
    image.filename = getattr(pil_image, 'filename', '')
    if image.filename:
        pil_image.filename = None
    return image
 
