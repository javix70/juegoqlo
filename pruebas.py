try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


import glob
import pyautogui
import csv
import cv2 as cv
import numpy as np

def category():
    categoryListDick = [{'Alquimista':11},
                        {'Animales':11},
                        {'Campesinos':3},
                        {'Carniceros y cazadores':3},
                        {'Documentos':5},
                        {'Escultores':3},
                        {'Figuras':1},
                        {'Hada artificial':1},
                        {'Herreros':9},
                        {'Joyero':2},
                        {'Leñadores':5},
                        {'Manitas':4},
                        {'Milicia':1},
                        {'Mineros':5},
                        {'Objetos de apariencia':5},
                        {'Panaderos':2},
                        {'Pescadores y pescaderos':3},
                        {'Piedras de alma':2},
                        {'Recursos':28},
                        {'Runas':1},
                        {'Sastres':3}, 
                        {'Trofeos':2},
                        {'Zapatero':2}]
    pass

def Locate_category_on_screen():
    #abrir path locateonscreen(la primera imagen- a la ultima) yield.
    pass

def screenshot():
    #sacar screenshot con region
    pass

def listar_imagenes():
    image_list = []
    for filename in glob.glob('./imagenes/*.png'): #assuming gif
        im=Image.open(filename)
        image_list.append(im)
    return image_list  

def abrir_imagen(image_list):  
    #read imagen
    for i in image_list:
        img = cv.imread(i)    
        yield img

def remove_nise_imagen():

    for img in abrir_imagen():
        path_img= './imagenes/'
        img_cv = path_img + img

        #convert RGB to HSV
        img_hsv = cv.cvtColor(img_cv, cv.COLOR_BGR2HSV) 

        # define range of white color in hsv
        lower_white = np.array([0,0,172], dtype=np.uint8)
        upper_white = np.array([255,9,255], dtype=np.uint8)

        #Threshold the HSV image to get only white colors
        mask = cv.inRange(img_hsv, lower_white, upper_white)

        #Bitwise-AND mask and original image
        res = cv.bitwise_and(img_cv,img_cv, mask = mask)
        invert_res = 255 - res
        # cv.imwrite("./imagenes/invertidos/" + img + ".png",invert_res) #por si queremos guardar las imagenes invertidas.

        return invert_res

def capture_texto(invert_res):
    custom_config = 'spa+spa1 --psm 6'
    txt = pytesseract.image_to_string(invert_res,lang=custom_config)
    
def tokenizar_archivo():
    pass
