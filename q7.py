import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/einstein.png', cv.IMREAD_GRAYSCALE)

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) 
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

im_x = cv.filter2D(img_orig, cv.CV_64F, sobel_x)
im_y = cv.filter2D(img_orig, cv.CV_64F, sobel_y)

fig, ax = plt.subplots (1, 2, figsize=(12, 6))
ax[0].imshow(im_x, cmap='gray')
ax[0].set_title('Sobel X (Using filter2D)')  
ax[0].axis('off')
ax[1].imshow(im_y, cmap='gray')
ax[1].set_title('Sobel Y (Using filter2D)')
ax[1].axis('off')

plt.show()