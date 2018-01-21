import cv2


# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/trex.png')
cv2.imshow("Original", image)

# Flip the image horizontally
flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)

# Flip the image vertically
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

# Flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
