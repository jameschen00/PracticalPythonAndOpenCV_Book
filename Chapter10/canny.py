import cv2


# Load the image, convert it to greyscale, and blur it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/coins.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow("Blurred", image)

# Canny Edge Detection
# gradient < threshold1 != edge
# threshold1 < gradient < threshold2 = edge/not-edge (based on 'connections')
# gradient > threshold2 = edge
canny = cv2.Canny(image, 30, 150)
cv2.imshow("Canny", canny)
cv2.waitKey(0)
