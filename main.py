#Image Compressor 

#step 1
import PIL
from PIL import Image
from tkinter.filedialog import *

#step2
file_path=askopenfilename()
img = PIL.Image.open(file_path)
myHeight,myWidth=img.size

#step3
img = img.resize((myHeight,myWidth),PIL.Image.LANCZOS)
save_path=asksaveasfilename()
img.save(save_path+"img.jpg")
