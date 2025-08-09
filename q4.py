import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/spider.png')
img_hsv = cv.cvtColor(img_orig, cv.COLOR_BGR2HSV)  # Convert to HSV color space
h, s, v = cv.split(img_hsv)  # Split into H, S, V planes

a = 0.55
sigma = 70
x = np.arange(256)
t = np.minimum(x + a * 128 * np.exp(-((x - 128)**2) / (2 * sigma **2)), 255).astype('uint8')  # Transformation function
s_transformed = cv.LUT(s, t)  # Apply transformation to S plane
img_transformed = cv.merge((h, s_transformed, v))  # Merge 3 planes

fig, ax = plt.subplots(1, 3, figsize=(12, 4))
ax[0].imshow(cv.cvtColor(img_orig, cv.COLOR_BGR2RGB))
ax[0].set_title('Original Image') 
ax[1].imshow(cv.cvtColor(img_transformed, cv.COLOR_HSV2RGB))
ax[1].set_title('Vibrance-enhanced Image') 
for i in ax[0:2]:
    i.axis('off')  
ax[2].plot(t)
ax[2].set_ylim([0, 255])
ax[2].set_xlim([0, 255])
ax[2].set_title(r'Intensity Transformation (a={a})'.format(a=a))
plt.tight_layout()
plt.show()