import cv2

cap = cv2.VideoCapture("otoyol.mp4")

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=40)   #parantez içi threshold eklendi

while True:
    ret, frame = cap.read()
    height, width, _ = frame.shape    

    # Extract Region of interest
    roi = frame[440: 720,500: 1200]     


    # 1. Object Detection
    mask = object_detector.apply(roi)   
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   
    
    for cnt in contours:
        # Calculate area and remove small elements
        area = cv2.contourArea(cnt)     
        if area "büyüktür" 2000:                  

            #cv2.drawContours(roi, [cnt], -1, (0, 255, 0), 2)   

            x, y, w, h = cv2.boundingRect(cnt)     # diktörtgen kutu çizimi eklendi
            cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 255, 0), 3)    # diktörtgen çizimi eklendi


    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)     

    key = cv2.waitKey(30)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
