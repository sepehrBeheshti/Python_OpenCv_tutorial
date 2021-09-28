from cv2 import *
import keyboard

c = VideoCapture(0)
while True:
  s, img = c.read()
  # imgCanny = cv2.Canny(img, 50, 100)
  cv2.imshow("Webcam", img)
  # if cv2.waitKey(1) & 0xFF == ord("q"):
    # break
  cv2.waitKey(1)
  if keyboard.is_pressed("q"):
    quit()
