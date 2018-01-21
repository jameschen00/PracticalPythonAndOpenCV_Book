import numpy as np
import cv2


# Initialize the canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# Draw a green line
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a red line
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a green rectangle
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a red rectangle (thickness=5)
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw a blue rectangle (filled)
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Reset the canvas with circles with increasing radii
canvas = np.zeros((300, 300, 3), dtype="uint8")
(center_x, center_y) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)

for r in range(0, 175, 25):
    cv2.circle(canvas, (center_x, center_y), r, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# Draw 25 random circles
for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist()
    point = np.random.randint(0, high=300, size=(2,))

    # Draw the random circle
    cv2.circle(canvas, tuple(point), radius, color, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
