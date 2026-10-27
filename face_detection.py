import cv2

#Load the Haar Cascade face detection model
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


#Start webcam(0 = default camera)
cap = cv2.VideoCapture(0)         #capture

while True:
    #Read frame from webcam
    ret, frame = cap.read()      #indicates front camera, ret = return it indicates whether it is successfull or not reading whereas frame reads the images
    
    #Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )
    #Draw Rectangle around faces
    for(x,y,w,h) in faces:      
        cv2.rectangle(
            frame,
            (x,y),
            (x + w, y + h),
            (0, 255, 0),   #it is the color--> green, we can take any combination of numbers 
            2    #it is the width of the rectangle
        ) 
    #show output window
    cv2.imshow("Face Detection", frame)
    
    #press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
#Release camera and close windows 
cap.release()
cv2.destroyAllWindows()