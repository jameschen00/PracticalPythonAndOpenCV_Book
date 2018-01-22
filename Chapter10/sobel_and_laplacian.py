import numpy as np
import cv2


# Load the image, convert it to greyscale, and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Compute the Laplacian of the image (using floats due to positive/negative slopes in colour transitions)
lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(0)

# Compute gradients along the X and Y axis, respectively
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)

# Convert to an 8-bit unsigned integer
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

# We can combine our Sobel gradient images using bitwise 'OR'
sobel_combined = cv2.bitwise_or(sobel_x, sobel_y)

# Show our Sobel images
cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel_combined)
cv2.waitKey(0)
