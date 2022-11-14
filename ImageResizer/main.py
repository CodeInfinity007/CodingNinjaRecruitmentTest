import cv2

file_name = input("Enter file name with extension: ")
new_height = int(input("Enter new height: "))
new_width = int(input("Enter new height: "))

img = cv2.imread(file_name)

# Get original Dimensions
print(f"Original Dimensions : {img.shape}")

# Resizing
rez_img = cv2.resize(img, (new_height, new_width))
print(f"Resized Dimensions : {rez_img.shape}")
cv2.imwrite('resized_imaged.jpg', rez_img)

cv2.imshow('Resized Image',rez_img)
cv2.imshow("Original Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
