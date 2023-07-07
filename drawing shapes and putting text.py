import cv2 as cv
import numpy as np

#lets try to create an empty image
blank = np.zeros((500,500,3),dtype='uint8') #uint8 is basically image
'''#painting the image red
blank[:]=0,0,255 # in CV it is BGR means blue, green and red
cv.imshow('Coloured image',blank)
cv.waitKey()'''


#drawning a rectangle
cv.rectangle(blank,(0,0),(250,250),(255,0,0),thickness=cv.FILLED) #-1 is also used for the same
cv.imshow('rectangle',blank)
#circle
cv.circle(blank,(250,250),40,(0,0,255),thickness=3)
cv.imshow('Circle',blank)
#draw a line
cv.line(blank,(0,0),(255,250),(0,255,0),thickness=5)
cv.imshow('line',blank)

#write text on a image
cv.putText(blank,'Hello',(350,400),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,0),2)
cv.imshow('Text in image',blank)
cv.waitKey()
