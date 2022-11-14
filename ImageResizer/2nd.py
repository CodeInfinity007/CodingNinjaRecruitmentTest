import cv2

img = cv2.imread('1.jpg')

# Get original Dimensions
print(f"Original Dimensions : {img.shape}")

# Resizing
rez_img = cv2.resize(img, (1920, 1080))

# Get Resized Dimensions
print(f"Resized Dimensions : {rez_img.shape}")

# Save Resized image in root directory
cv2.imwrite('resized_imaged.jpg', rez_img)