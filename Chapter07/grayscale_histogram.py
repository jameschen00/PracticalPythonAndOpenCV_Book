import matplotlib.pyplot as plt
import cv2


# Load the image, convert it to greyscale, and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# Construct a greyscale histogram
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

# Plot the histogram
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()
cv2.waitKey(0)
