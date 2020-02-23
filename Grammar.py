import pytesseract, language_check      
from pil import Image     

file = 'humanbotics.PNG'
# opening an image from the source path 
img = Image.open(file)
dot = file.index(".")

name = file[0:dot]

tool = language_check.LanguageTool('en-US')

print("loaded")

# path where the tesseract module is installed 
pytesseract.pytesseract.tesseract_cmd ='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img)    
# write text in a text file and save it to source path    
with open(name + '.txt',mode ='w') as file:      
    file.write(result)
    
print("image read")

with open(name + '.txt',mode ='r') as file:      
    orig = file.read()

matches = tool.check(orig)
orig = orig.replace(orig, language_check.correct(orig, matches))

with open(name + '.txt',mode ='w') as file:      
    file.write(orig)

print("finished")
