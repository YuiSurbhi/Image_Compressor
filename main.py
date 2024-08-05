#Image Compressor 

#step 1
# Import the necessary modules from PIL (Python Imaging Library) and tkinter
import PIL
from PIL import Image
from tkinter.filedialog import *

#step2
# Open a file dialog to select an image file
file_path=askopenfilename()

# Open the selected image file using PIL
img = PIL.Image.open(file_path)

# Get the height and width of the image
myHeight,myWidth=img.size

#step3
# Resize the image to the same dimensions as the original image using LANCZOS resampling
img = img.resize((myHeight,myWidth),PIL.Image.LANCZOS)

# Open a file dialog to specify the path and filename to save the resized image
save_path=asksaveasfilename()

# Save the resized image to the specified path with a .jpg extension
# Note: Ensure the user provides the extension or the filename ends with .jpg
img.save(save_path+"img.jpg")
