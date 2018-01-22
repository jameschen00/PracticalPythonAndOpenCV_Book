import numpy as np
import cv2


# Load the image and convert it to greyscale
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization to stretch the contrast of our image
eq = cv2.equalizeHist(image)

# Show our images
cv2.imshow("Histogram Equalization", np.hstack([image, eq]))
cv2.waitKey(0)
