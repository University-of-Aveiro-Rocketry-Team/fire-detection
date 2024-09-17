from detection import Detector
import cv2
from PIL import Image

MODEL_PATH='fire-models/fire_l.pt'

def main():
	detector = Detector(MODEL_PATH)
	prediction, results = detector.image('tests/fire/woolsey12.jpg')

	print(results)
	detector.save_prediction(prediction, 'woolsey12.jpg')

if __name__ == '__main__':
	main()