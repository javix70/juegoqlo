try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

import pyautogui
import csv
import cv2 as cv
import numpy as np

def nothing(x):
    pass

#crea GUI de paleta de colores
"""
cv.namedWindow("Tracking")
cv.createTrackbar("LH","Tracking",0,255,nothing)
cv.createTrackbar("LS","Tracking",0,255,nothing)
cv.createTrackbar("LV","Tracking",0,255,nothing)
cv.createTrackbar("UH","Tracking",255,255,nothing)
cv.createTrackbar("US","Tracking",255,255,nothing)
cv.createTrackbar("UV","Tracking",255,255,nothing)
"""

#read imagen
img_cv = cv.imread(".\imagenes\obv.png")
custom_config = 'spa+spa1 --psm 6'

#convert RGB to HSV
img_hsv = cv.cvtColor(img_cv, cv.COLOR_BGR2HSV) 

#invocación de la GUI de colores, van en los parametros de lowe and upper
"""while True:
    img_cv = cv.imread(".\imagenes\pene3.png")
    img_hsv = cv.cvtColor(img_cv, cv.COLOR_BGR2HSV) 

    l_h  = cv.getTrackbarPos("LH","Tracking")
    l_s  = cv.getTrackbarPos("LS","Tracking")
    l_v  = cv.getTrackbarPos("LV","Tracking")
    u_h  = cv.getTrackbarPos("UH","Tracking")
    u_s  = cv.getTrackbarPos("US","Tracking")
    u_v  = cv.getTrackbarPos("UV","Tracking")"""

# define range of white color in hsv
lower_white = np.array([0,0,172], dtype=np.uint8)
upper_white = np.array([255,9,255], dtype=np.uint8)

#Threshold the HSV image to get only white colors
mask = cv.inRange(img_hsv, lower_white, upper_white)

#Bitwise-AND mask and original image
res = cv.bitwise_and(img_cv,img_cv, mask = mask)
invert_res = 255 - res

# # Mostrar ventanas
# cv.imshow('invert',invert_res)
# cv.imshow('frame',img_cv)
# cv.imshow('mask',mask)
# cv.imshow('res',res)


txt = pytesseract.image_to_string(invert_res,lang=custom_config)
print(txt)

# with open("output.txt","a") as file:
#     file.write(txt)

#encierra caracteres en boxes a travez de dict
d = pytesseract.image_to_data(img_cv, output_type=Output.DICT,lang=custom_config )

n_boxes = len(d['text'])
for i in range(n_boxes):
    if int(d['conf'][i]) > 60:
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img_cv = cv.rectangle(img_cv, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('img_cv', img_cv)
cv.waitKey(0)

#encerrar en boxes los caracteres 
h,w,c = img_cv.shape
boxes = pytesseract.image_to_boxes(img_cv)
for b in boxes.splitlines():
    b = b.split(' ')
    img_cv = cv.rectangle(img_cv, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0),2)

cv.imshow('img', img_cv)
cv.waitKey(0)