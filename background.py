import cv2
#This is my webcam.
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, back = cap.read() #Here I am simply reading from my webcam.
    if ret:
        #back is what the webcam is reading
        cv2.imshow("image", back)
        if cv2.waitKey(5) == ord('q'):
            #save the image.
            cv2.imwrite('image.jpg', back)
            break

cap.release()
cv2.destroyAllWindows()
