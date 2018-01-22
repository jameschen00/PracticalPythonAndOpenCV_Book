import numpy as np
import cv2

# Load the image, convert it to greyscale, and blur it slightly
image = cv2.imread('C:/PythonProjects/PracticalPythonAndOpenCV_Book/images/coins.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
cv2.imshow("Image", image)

# Apply edge detection
edged = cv2.Canny(blurred, 30, 150)
cv2.imshow("Edges", edged)

# Find contours in the edged image.
(_, contours, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# How many contours did we find?
print("{} coins in this image".format(len(contours)))

# Let's highlight the coins in the original image by drawing a green circle around them
coins = image.copy()
cv2.drawContours(coins, contours, -1, (0, 255, 0), 2)
cv2.imshow("Coins", coins)
cv2.waitKey(0)

# Loop over each contour
for (i, c) in enumerate(contours):
    # We can compute the 'bounding box' for each contour
    (x, y, w, h) = cv2.boundingRect(c)

    # Extract the contour
    print("Coin #{}".format(i + 1))
    coin = image[y:y + h, x:x + w]
    cv2.imshow("Coin", coin)

    # Construct a mask for the coin by finding the minumum enclosing circle of the contour
    mask = np.zeros(image.shape[:2], dtype="uint8")
    ((center_x, center_y), radius) = cv2.minEnclosingCircle(c)
    cv2.circle(mask, (int(center_x), int(center_y)), int(radius), 255, -1)
    mask = mask[y:y + h, x:x + w]
    cv2.imshow("Masked Coin", cv2.bitwise_and(coin, coin, mask=mask))
    cv2.waitKey(0)
