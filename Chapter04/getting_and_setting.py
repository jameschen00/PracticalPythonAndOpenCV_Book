import cv2


# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/trex.png')
cv2.imshow("Original", image)

# Check pixel value at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - R: {}, G: {}, B: {}".format(r, g, b))

# Change the pixel value at (0, 0) to red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - R: {}, G: {}, B: {}".format(r, g, b))

# Get the top-left corner
corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

# Make the top-left corner green
image[0:100, 0:100] = (0, 255, 0)

# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
