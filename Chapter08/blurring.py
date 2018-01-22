import numpy as np
import cv2

# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
cv2.imshow("Original", image)

# Averaging blurring (Mean)
blurred = np.hstack([cv2.blur(image, (3, 3)),
                     cv2.blur(image, (5, 5)),
                     cv2.blur(image, (7, 7))])
cv2.imshow("Averaged", blurred)
cv2.waitKey(0)

# Gaussian blurring (Weighted Mean)
blurred = np.hstack([cv2.GaussianBlur(image, (3, 3), 0),
                     cv2.GaussianBlur(image, (5, 5), 0),
                     cv2.GaussianBlur(image, (7, 7), 0)])
cv2.imshow("Gaussian", blurred)
cv2.waitKey(0)

# Median Blurring (for removing 'salt & pepper' noise)
blurred = np.hstack([cv2.medianBlur(image, 3),
                     cv2.medianBlur(image, 5),
                     cv2.medianBlur(image, 7)])
cv2.imshow("Median", blurred)
cv2.waitKey(0)

# Bilateral Blurring (Reduce noise and preserve edges)
blurred = np.hstack([cv2.bilateralFilter(image, 5, 21, 21),
                     cv2.bilateralFilter(image, 7, 31, 31),
                     cv2.bilateralFilter(image, 9, 41, 41)])
cv2.imshow("Bilateral", blurred)
cv2.waitKey(0)
