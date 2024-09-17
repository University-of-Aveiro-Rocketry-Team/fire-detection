import cv2
import os
from ultralytics import YOLO
from PIL import Image

class Detector:
	def __init__(self, model_path):
		self.model = YOLO(model_path)
		self.conf = 0.25
		self.iou = 0.45

		self.save_path = 'results'

	def image(self, image_path):
		img = cv2.imread(image_path)

		res = self.model.predict(
			img,
			conf=self.conf,
			iou=self.iou,
			device='cpu'
		)

		class_name = self.model.model.names
		classes = res[0].boxes.cls
		class_counts = {}

		for c in classes:
			c = int(c)
			class_counts[class_name[c]] = class_counts.get(class_name[c], 0) + 1

		res_image = res[0].plot()
		res_image = cv2.cvtColor(res_image, cv2.COLOR_BGR2RGB)

		return res_image, class_counts

	def save_prediction(self, img, filename):
		# create save path if not exists
		if not os.path.exists(self.save_path):
			os.makedirs(self.save_path)

		prediction = Image.fromarray(img)
		prediction.save(f'{self.save_path}/{filename}')