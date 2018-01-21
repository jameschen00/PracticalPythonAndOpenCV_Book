import numpy as np
import cv2

# Draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
cv2.imshow("Rectangle", rectangle)

# Draw a circle
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
cv2.imshow("Circle", circle)

# 'AND'
bitwise_and = cv2.bitwise_and(rectangle, circle)
cv2.imshow("AND", bitwise_and)
cv2.waitKey(0)

# 'OR'
bitwise_or = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwise_or)
cv2.waitKey(0)

# 'XOR'
bitwise_xor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwise_xor)
cv2.waitKey(0)

# 'NOT'
bitwise_not = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwise_not)
cv2.waitKey(0)
