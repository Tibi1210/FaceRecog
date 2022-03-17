import cv2 as cv

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_eye.xml')
cap = cv.VideoCapture(0, cv.CAP_DSHOW)
asd = 0

while True:

    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=4)

    for (x, y, w, h) in face_rects:
        image3 = frame[y:y + h, x:x + int(float(w)/2)]
        image4 = frame[y:y + h, x+int(float(w)/2):x + w]

        if asd == 0:
            rect_4_eyes = image3
            cv.imshow("image 1", image3)
        else:
            rect_4_eyes = image4
            cv.imshow("image 1", image4)

        cv.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 2)
        eyes = eye_cascade.detectMultiScale(
            image=rect_4_eyes, scaleFactor=1.05, minNeighbors=2)

    for (xe, ye, we, he) in eyes:
        center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
        radius = int((we + he) / 5)
        cv.circle(rect_4_eyes, center, radius, 255, 2)
        break
    cv.imshow('frame', frame)

    k = cv.waitKey(1)
    if k & 0xFF == ord('q'):
        break
    if k & 0xFF == ord('e'):
        if asd == 0:
            asd = 1
        else:
            asd = 0

cap.release()
cv.destroyAllWindows()
