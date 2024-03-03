import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

img_path = "/Users/hoangmac/ImageProcessing and Computer Vision/ImageProcessing/oil-and-gas-real.png"


img = cv2.imread(img_path)
print(img.shape)
plt.figure(figsize=(8, 6), dpi=1000)
fix_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.imshow(fix_img)

#Let's extract the three channels
R, G, B = fix_img[:,:,0], fix_img[ :,:,1 ],fix_img[:,:,2]
Y=0.299*R+0.587*G+0.114*B
Z = 0.2126 * R + 0.7152 * G + 0.0722 * B

plt.imshow(Y, cmap='gray')
plt.savefig('image_weighted_average_byhand.png')