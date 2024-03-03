import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = "/Users/hoangmac/ImageProcessing and Computer Vision/ImageProcessing/oil-and-gas-real.png"


def compute_gray_scale_factor_by_lightness_method(image_path):
    if not os.path.exists(image_path):
        return

    img = cv2.imread(image_path)
    R, G, B = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    min_r = np.min(R)
    min_g = np.min(G)
    min_b = np.min(B)

    max_r = np.max(R)
    max_g = np.max(G)
    max_b = np.max(B)
    return 0.5*(min(min_r,min_g, min_b) + max(max_r, max_g, max_b))

# Load an color image in grayscale
img = cv2.imread(image_path)
# gray_scale = compute_gray_scale_factor_by_lightness_method(image_path)
print(img.shape)
# fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
B, G, R = img[:, :, 0], img[:, :, 1], img[:, :, 2]

# lightnessImgGray = gray_scale*R + gray_scale*G + gray_scale*B

imgGray = 0.299 * R + 0.587 * G + 0.114 * B

Average_Gray = B / 3 + G / 3 + R / 3
Weighted_Gray = (0 * B) + (0 * G) + (1 * R)

# plt.imshow(imgGray, cmap="gray")

# Show the image
cv2.imshow('image', imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
# https://www.baeldung.com/cs/convert-rgb-to-grayscale