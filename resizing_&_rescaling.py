import cv2 as cv
def rescaleFrame(frame,scale = 0.75):
    # this will work for images,video and live videos
    width = int(frame.shape[1]*scale) #frame.shape[1] is width of the image
    height = int(frame.shape[0]*scale) #frame.shape[1] is height of the image
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)
'''
def changeRes(width,height):
    #this will only work for live videos
    capture.set(3,width)
    capture.set(4,height)
'''

capture = cv.VideoCapture('C:\\Users\\Lenovo\\OneDrive\\Desktop\\ML and DL\\Computer Vision\\black_hole_video.mp4')
while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=0.4)

    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey()