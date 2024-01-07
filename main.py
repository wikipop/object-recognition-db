import cv2
import time

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
ginger_cap = cv2.VideoCapture('video (2160p).mp4')


def detect_from_video(cap: cv2.VideoCapture, cascade: cv2.CascadeClassifier):
    start = time.time()
    frame_number = 1

    while cap.isOpened():
        _, img = cap.read()
        img = cv2.resize(img, (1280, 720))
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        detected = cascade.detectMultiScale(gray_img, scaleFactor=1.25, minNeighbors=10)

        for x, y, w, h in detected:
            img_to_save = img[y:y + h, x:x + w]
            cv2.imwrite(f"detected/{frame_number}.jpg", img_to_save)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv2.imshow("Output", img)

        print("fps: ", round(frame_number / (time.time() - start)))
        frame_number += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


detect_from_video(ginger_cap, eye_cascade)
