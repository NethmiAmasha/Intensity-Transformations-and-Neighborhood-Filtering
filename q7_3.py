import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

img_orig = cv.imread('a1images/einstein.png', cv.IMREAD_GRAYSCALE)


# --- Using seperable filters ---

array1 = np.array([[1, 2, 1]])
array2 = np.array([[1, 0, -1]])

im_x_intermediate = cv.filter2D(img_orig, cv.CV_64F, array1.reshape(3, 1))
im_x = cv.filter2D(im_x_intermediate, cv.CV_64F, array2)
im_y_intermediate = cv.filter2D(img_orig, cv.CV_64F, array2.reshape(3, 1))
im_y = cv.filter2D(im_y_intermediate, cv.CV_64F, array1)


fig, ax = plt.subplots (1, 2, figsize=(12, 6))
ax[0].imshow(im_x, cmap='gray')
ax[0].set_title('Sobel X (Using seperable filters)')  
ax[0].axis('off')
ax[1].imshow(im_y, cmap='gray')
ax[1].set_title('Sobel Y (Using seperable filters)')
ax[1].axis('off')

plt.show()