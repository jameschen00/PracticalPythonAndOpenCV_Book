import matplotlib.pyplot as plt
import numpy as np
import cv2


def plot_histogram(image, title, mask=None):
    # Grab the image channels, initialize the tuple of colors and the figure
    channels = cv2.split(image)
    colors = ("b", "g", "r")
    plt.figure()
    plt.title(title)
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")

    # Loop over the image channels
    for (channel, color) in zip(channels, colors):
        # Create a histogram for the current channel and plot it
        hist = cv2.calcHist([channel], [0], mask, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])


# Load the original image and plot a histogram for it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
cv2.imshow("Original", image)
plot_histogram(image, "Histogram for Original Image")

# Construct a mask for our image - WHITE for regions we want to EXAMINE
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (15, 15), (130, 100), 255, -1)
cv2.imshow("Mask", mask)

# Show the image
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("Applying the Mask", masked)

# Compute a histogram for the pixels in the masked region
plot_histogram(image, "Histogram for Masked Image", mask=mask)

# Show our plots
plt.show()
cv2.waitKey(0)
