import matplotlib.pyplot as plt
import cv2

# Load the image and show it
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/beach.png')
cv2.imshow("Original", image)

# Grab the image channels, initialize the tuple of colors and the figure
channels = cv2.split(image)
colors = ("b", "g", "r")
plt.figure()
plt.title("'Flattened' Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")

# Loop over the image channels
for (chan, color) in zip(channels, colors):
    # Create a histogram for the current channel and plot it
    hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# Plot a 2D color histogram for green and blue
fig = plt.figure()
ax = fig.add_subplot(131)
hist = cv2.calcHist([channels[1], channels[0]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and B")
plt.colorbar(p)

# Plot a 2D color histogram for green and red
ax = fig.add_subplot(132)
hist = cv2.calcHist([channels[1], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for G and R")
plt.colorbar(p)

# Plot a 2D color histogram for blue and red
ax = fig.add_subplot(133)
hist = cv2.calcHist([channels[0], channels[2]], [0, 1], None, [32, 32], [0, 256, 0, 256])
p = ax.imshow(hist, interpolation="nearest")
ax.set_title("2D Color Histogram for B and R")
plt.colorbar(p)

# Dimensionality of one of the 2D histograms
print("2D Histogram Shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# 3D color histogram shape
hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
print("3D Histogram Shape: {}, with {} values".format(hist.shape, hist.flatten().shape[0]))

# Show our plots
plt.show()
cv2.waitKey(0)
