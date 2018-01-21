import numpy as np
import imutils
import cv2


# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/trex.png')
cv2.imshow("Original", image)

# Translate the image 25 pixels to the right and 50 pixels down
matrix = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, matrix, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# Shift the image 50 pixels to the left and 90 pixels up
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Use our own function in to shift the image down 100 pixels
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
