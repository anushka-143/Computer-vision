import cv2
img = cv2.imread('C:\\Users\\Anushka Tomar\\Desktop\\computer vision\\Untitled.jpg')
cv2.imshow('image', img)

#converting it to gray scale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

#blur
blur = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow('blur',blur)

#Edge cascade
canny = cv2.Canny(img,125,175)
cv2.imshow('canny',canny)

#dilating the image
dilated = cv2.dilate(canny,(5,5),iterations=3)
cv2.imshow('dilated',dilated)

#eroding
eroded = cv2.erode(dilated,(3,3),iterations=1)
cv2.imshow('eroded',eroded)


# resize the image
resized = cv2.resize(img, (500, 500), interpolation = cv2.INTER_CUBIC)
cv2.imshow('resized', resized)
cv2.waitKey()




