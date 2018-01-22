import mahotas
import cv2


# Load the image, convert it to greyscale, and blur it slightly
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Image", image)

# Otsu Thresholding (assumes that are two 'peaks' in the greyscale histogram and uses them to compute a threshold
t = mahotas.thresholding.otsu(blurred)
print("Otsu's threshold: {}".format(t))

# Otsu Thresholding (using NumPy)
thresh = image.copy()
thresh[thresh > t] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Otsu", thresh)

# Riddler-Calvard Thresholding
t = mahotas.thresholding.rc(blurred)
print("Riddler-Calvard: {}".format(t))
thresh = image.copy()
thresh[thresh > t] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imshow("Riddler-Calvard", thresh)
cv2.waitKey(0)
