import time

import numpy as np
import cv2


class Detector:
    def __init__(self, cuda=False):
        self.img = None
        self.faceModel = cv2.dnn.readNetFromCaffe("classifiers/facemodel.prototxt",
                                                  caffeModel="classifiers/facemodel.caffemodel")

        if cuda:
            self.faceModel.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
            self.faceModel.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    def processImage(self, imgName):
        self.img = cv2.imread(imgName)
        self.img = cv2.resize(self.img, (900, 900))
        (self.height, self.width) = self.img.shape[:2]

        self.processFrame()

        cv2.imshow("Output", self.img)
        cv2.waitKey(0)

    def processVideo(self, videoName):
        cap = cv2.VideoCapture(videoName)

        start = time.time()
        frame_n = 1

        while cap.isOpened():
            ret, self.img = cap.read()
            self.img = cv2.resize(self.img, (1280, 720))
            (self.height, self.width) = self.img.shape[:2]

            self.processFrame()

            cv2.imshow("Output", self.img)

            frame_n += 1
            print("FPS: ", frame_n / (time.time() - start))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def processFrame(self):
        blob = cv2.dnn.blobFromImage(self.img, 1.0, (300, 300), (104.0, 177.0, 123.0),
                                     swapRB=False, crop=False)

        self.faceModel.setInput(blob)
        detections = self.faceModel.forward()

        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence < 0.5:
                continue

            box = detections[0, 0, i, 3:7] * np.array([self.width, self.height, self.width, self.height])
            (x, y, x1, y1) = box.astype("int")

            cv2.rectangle(self.img, (x, y), (x1, y1), (0, 255, 0), 2)
