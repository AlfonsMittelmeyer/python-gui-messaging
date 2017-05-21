from PIL import Image as Pil_Image
from PIL import ImageTk as Pil_ImageTk

def open(filename):
    global Pil_Imagefile
    Pil_Imagefile = filename
    return Pil_Image.open(filename)

def PhotoImage(pil_image):
    image = Pil_ImageTk.PhotoImage(pil_image)
    _image_dictionary[image] = Pil_Imagefile
    return image

def init(image_dict):
    global _image_dictionary
    _image_dictionary = image_dict
    
