import cv2


# Load the image, convert it to greyscale, and blur it slightly
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Simple Thresholding
(t, thresh) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary", thresh)

# Visualize only the coins in the image
cv2.imshow("Coins", cv2.bitwise_and(image, image, mask=thresh))
cv2.waitKey(0)
