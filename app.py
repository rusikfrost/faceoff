import cv2
import sys
#from PIL import Image
import numpy as np

from random import seed
from random import randint

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from bot import *

def main(argv):
	src = cv2.imread('_faces.jpg')
	h, w = src.shape[0:2]
	# получаем высоту и ширину изображения для 
	print(h, w)
	print("work it")
 
	# заполняем матрицу преобразования. сначала все нулями
	intrinsics = np.zeros((3, 3), np.float64)
 
	# матрица intrinsics
	intrinsics[0, 0] = 3500
	intrinsics[1, 1] = 3500
	intrinsics[2, 2] = 1.0
	intrinsics[0, 2] = w/2.
	intrinsics[1, 2] = h/2.
	print(intrinsics)
 
	newCamMtx = np.zeros((3, 3), np.float64)
	newCamMtx[0, 0] = 3500
	newCamMtx[1, 1] = 3500
	newCamMtx[2, 2] = 1.0
	newCamMtx[0, 2] = w/2.
	newCamMtx[1, 2] = h/2.
 
	dist_coeffs = np.zeros((1, 4), np.float64)
	dist_coeffs[0, 0] = randint(-500, -100)
	dist_coeffs[0, 1] = 1.0
	dist_coeffs[0, 2] = 1.0
	dist_coeffs[0, 3] = -0.0
	#print dist_coeffs
 
	map1, map2 = cv2.initUndistortRectifyMap(intrinsics, dist_coeffs, None, newCamMtx, src.shape[:2], cv2.CV_16SC2)
	res = cv2.remap(src, map1, map2, cv2.INTER_LINEAR)
	cv2.imwrite("Image_res.jpg", res)

	#new  Amatic-Bold.ttf

	font = ImageFont.truetype("Adigiana 2.ttf", 28, encoding="unic")
	text_position = (w*0.005, h*0.6)
	text_color = (255,255,255)
	text = 'this bot \n powered by  \n my anus'
	img = Image.open('Image_res.jpg')

	draw = ImageDraw.Draw(img)

	draw.text(text_position, text, text_color, font)

	img.save('blank_with_text.jpg')
	sendThisFuckinPhoto()

def fuckThePhoto(path_img):
	#imagePath = sys.argv[1]
	imagePath = path_img
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
	faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.3,
	minNeighbors=3,
	minSize=(30, 30)
	)
	print("[INFO] Found {0} Faces.".format(len(faces)))
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
		roi_color = image[y:y + h, x:x + w]
		print("[INFO] Object found. Saving locally.")
		#cv2.imwrite(str(w) + str(h) + '_faces.jpg', roi_color)
		cv2.imwrite('_faces.jpg', roi_color)
		status = cv2.imwrite('faces_detected.jpg', image)
		print("[INFO] Image faces_detected.jpg written to filesystem: ", status)
	#if __name__ == '__main__':
		main(sys.argv)
		
			#new

		 
			#cv2.imshow("Image_res", res)
			#cv2.imshow("Image_origin", src)
			#cv2.waitKey(0)

