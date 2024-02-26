import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = r"C:/Users/HoangNguyen/OneDrive/Pictures/figma.png"
# image_path = r"C:/Users/HoangNguyen/OneDrive/Pictures/vst9f4nhuj2bdgvxlelo.png"
# img = cv2.imread(r"C:\Users\HoangNguyen\OneDrive\Pictures\vst9f4nhuj2bdgvxlelo.png", cv2.IMREAD_GRAYSCALE)
#
# cv2.imshow('image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# Load an color image in grayscale
img = cv2.imread(image_path)

R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
# imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
imgGray = (R + G + B) / 3
imgGray = 0.299 * R + 0.587 * G + 0.114 * B

Average_Gray = B / 3 + G / 3 + R / 3
Weighted_Gray = (0 * B) + (0 * G) + (1 * R)

# plt.imshow(imgGray, cmap="gray")

# Show the image
cv2.imshow('image', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# https://www.baeldung.com/cs/convert-rgb-to-grayscale