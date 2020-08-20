import cv2
import os
i=0
print ( str(i) )
i+=1
print ( str(i) )
i+=1
print ( str(i) )
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
body_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
#smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
def blur_face(img):
	(h, w) = img.shape[:2]
	dW = int(w / 3.0)
	dH = int(h / 3.0)
	if dW % 2 == 0:
		dW -= 1
	if dH % 2 == 0:
		dH -= 1
	return cv2.GaussianBlur(img, (dW, dH), 0)
i=0
j=0
p=0
while True:
	rec, img = capture.read()
	faces = face_cascade.detectMultiScale(img, scaleFactor=2.0, minNeighbors=5, minSize=(20, 20))
	for (x, y, w, h) in faces:
		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)
		k = cv2.waitKey(10) & 0xFF
		if k == 13:
				i += 1
				cv2.imwrite("face"+str(i)+".png", img[y:y+h, x:x+w])
				os.system("mv ./face"+str(i)+".png ./faces")

		#img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])
	eyes = eye_cascade.detectMultiScale(img, scaleFactor=2.0, minNeighbors=5, minSize=(20, 20))
	for (x, y, w, h) in eyes:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
		k = cv2.waitKey(10) & 0xFF
		if k == 32:
			j+=1
			cv2.imwrite("eye"+str(j)+".png", img[y:y+h, x:x+w])
			os.system("mv ./eye"+str(j)+".png ./eyes")
		#img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])
	bodys = body_cascade.detectMultiScale(img, scaleFactor=2.0, minNeighbors=5, minSize=(75, 75))
	for (x, y, w, h) in bodys:
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)
		k = cv2.waitKey(10) & 0xFF
		if k == int(p):
			p+=1
			cv2.imwrite("body"+str(p)+".png", img[y:y+h, x:x+w])
			os.system("mv ./body"+str(p)+".png ./bodys")
		#img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])
#	smiles = smile_cascade.detectMultiScale(img, scaleFactor=2.0, minNeighbors=5, minSize=(20, 20))
#	for (x, y, w, h) in smiles:
#		cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#		#img[y:y+h, x:x+w] = blur_face(img[y:y+h, x:x+w])
	cv2.imshow('hello',img)
	k = cv2.waitKey(10) & 0xFF
	if k == 27:
		break

capture.release()
cv2.destroyAllWindows()
