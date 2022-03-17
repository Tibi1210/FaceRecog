import cv2 as cv

face_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_eye.xml')
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    _, frame = cap.read()
    face_rects = face_cascade.detectMultiScale(
        frame, scaleFactor=1.2, minNeighbors=4)

    for (x, y, w, h) in face_rects:
        image = frame[y:y + h, x:x + w]
        rect_4_eyes = image
        cv.rectangle(frame, (x, y), (x+w, y + h), (0, 255, 0), 2)
        eyes = eye_cascade.detectMultiScale(
            image=rect_4_eyes, scaleFactor=1.05, minNeighbors=2)

    for (xe, ye, we, he) in eyes:
        center = (int(xe + 0.5 * we), int(ye + 0.5 * he))
        radius = int((we + he) / 5)
        cv.circle(rect_4_eyes, center, radius, 255, 2)
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
        discharge_weapon = False
        break

    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
