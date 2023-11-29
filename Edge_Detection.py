import cv2
import numpy as np

# Read the input image
img = cv2.imread('monochrome_traced_image.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Harris Corner Detection
dst = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Threshold for an optimal value, it may vary depending on the image.
img[dst > 0.01 * dst.max()] = [0, 0, 255]  # Mark detected corners in red

# Display the results
cv2.imshow('Original Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

