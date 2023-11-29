import cv2
import numpy as np

def save_image(image, filename):
    cv2.imwrite(filename, image)
    print(f"Image saved as '{filename}'.")

# Read the resized image
image = cv2.imread(r'C:\Users\kshitij\OneDrive\Desktop\WhatsApp Image 2023-11-28 at 18.20.45_71d23d00.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray, 50, 150)

# Find contours in the image
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a black canvas to draw the traced image
traced_image = np.zeros_like(image)

# Draw the contours on the traced image with a monochrome color (e.g., white)
color = (255, 255, 255)  # White color
cv2.drawContours(traced_image, contours, -1, color, 1)

# Display the original image and the traced image in separate windows
cv2.imshow('Original Image', image)
cv2.imshow('Monochrome Traced Image', traced_image)

# Save the traced image to your computer
save_image(traced_image, 'monochrome_traced_image.jpg')

# Wait for a key press and close the windows on pressing the 'Esc' key
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
