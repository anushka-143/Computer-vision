import cv2
input_image = cv2.imread('C:\\Users\\Lenovo\\OneDrive\\Desktop\\ML and DL\\Computer Vision\\Untitled.jpg')

#to display the image we use imshow(title name of the window,input)
cv2.imshow('Test image',input_image)

'''the 'waitkey' allows us to input information when a image window is open,by leaving it blank it just waits for any
 key to be pressed before continuing. by placing numbers(except 0) we can specify a delay for how long you want to keep
the window open, time is in milliseconds here'''

cv2.waitKey()

cv2.destroyAllWindows()
print(input_image.shape)
cv2.imwrite('output.png',input_image)