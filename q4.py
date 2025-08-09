import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/spider.png')
img_hsv = cv.cvtColor(img_orig, cv.COLOR_BGR2HSV)  # Convert to HSV color space
h, s, v = cv.split(img_hsv)  # Split into H, S, V channels

a = 0.5 
sigma = 70
x = np.arange(256)
t = np.array([x + a * 128 * np.exp(-(x - 128)**2) / (2 * sigma **2), 255]).astype('unit8')  # Transformation function
s_transformed = cv.LUT(s, t)  # Apply transformation to S channel
img_transformed = cv.merge((h, s_transformed, v))  # Merge channels back

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(cv.cvtColor(img_orig, cv.COLOR_BGR2RGB))
ax[0].set_title('Original Image') 
ax[1].imshow(cv.cvtColor(img_transformed, cv.COLOR_HSV2RGB))
ax[1].set_title('Transformed Image')   
ax[2].plot(t)
ax[2].set_ylim([0, 255])
ax[2].set_xlim([0, 255])
ax[2].set_title('Intensity Transformation')