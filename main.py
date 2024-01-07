from Detector import Detector

detector = Detector(cuda=True)

#.processImage("data/wojciechPiech.jpg")
detector.processVideo("data/video (2160p).mp4")