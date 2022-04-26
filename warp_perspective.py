import cv2
import numpy as np

img = cv2.imread("Resources/cards2.jpg")

width, height = 215,235
points = np.float32([[103,229],[188,230],[101,109],[187,109]]) #take the points using paint, looka at the left corner bottom
points2 = np.float32([[0,0],[width,0],[0,height],[width, height]])
matrix = cv2.getPerspectiveTransform(points,points2)
imgOutput = cv2.warpPerspective(img, matrix,(width, height))

cv2.imshow("Image", img)
cv2.imshow("Output", imgOutput)
cv2.waitKey(0)