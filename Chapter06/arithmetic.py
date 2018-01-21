import numpy as np
import cv2


# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/trex.png')
cv2.imshow("Original", image)

# Demonstrate 'unsigned integers' for addition and subtraction using OpenCV
print("Max of 255: {}".format(cv2.add(np.uint8([200]), np.uint8([100]))))
print("Min of 0: {}".format(cv2.subtract(np.uint8([50]), np.uint8([100]))))

# Demonstrate 'unsigned intergers' for addition and subtraction using NumPy
print("wrap around: {}".format(np.uint8([200]) + np.uint8([100])))
print("wrap around: {}".format(np.uint8([50]) - np.uint8([100])))

# Increase the intensity of all pixels in our image by 100 (to make it brighter)
mask = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image, mask)
cv2.imshow("Added", added)

# Subtract 50 from all pixels in the image and make it darker:
M = np.ones(image.shape, dtype="uint8") * 50
subtracted = cv2.subtract(image, M)
cv2.imshow("Subtracted", subtracted)
cv2.waitKey(0)
