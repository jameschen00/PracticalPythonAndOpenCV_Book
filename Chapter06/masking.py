import numpy as np
import cv2


# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
cv2.imshow("Original", image)

# Construct a mask with a 150x150 square
mask = np.zeros(image.shape[:2], dtype="uint8")
(c_x, c_y) = (image.shape[1] // 2, image.shape[0] // 2)
cv2.rectangle(mask, (c_x-75, c_y-75), (c_x+75, c_y+75), 255, -1)
cv2.imshow("Mask", mask)

# Apply our mask
masked = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# Make a circular mask with a radius of 100 pixels
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask, (c_x, c_y), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)
