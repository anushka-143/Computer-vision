import cv2 as cv

capture = cv.VideoCapture('C:\\Users\\Lenovo\\OneDrive\\Desktop\\ML and DL\\Computer Vision\\black_hole_video.mp4')
#lets read video frame by frame
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):#0xFF==ord('d') means window will only get closed if 'd' key is pressed
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey()


