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



# sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]) 
# sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

# --- Using a custom function ---

# def filter(image, kernel):
#     k_hh, k_hw = math.floor(kernel.shape[0]/2), math.floor(kernel.shape[1]/2)
#     h, w = image.shape
#     image_float = cv.normalize(image.astype('float'), None, 0.0, 1.0, cv.NORM_MINMAX)
#     result = np.zeros(image.shape, 'float')
    
#     for m in range(k_hh, h - k_hh):
#         for n in range(k_hw, w - k_hw):            
#             result[m,n] = np.dot(image_float[m-k_hh:m + k_hh + 1, n - k_hw : n + k_hw + 1].flatten(), kernel.flatten())   
#     return result

# im_x = filter(img_orig, sobel_x)
# im_y = filter(img_orig, sobel_y)



# --- Using filter2D ---

# im_x = cv.filter2D(img_orig, cv.CV_64F, sobel_x)
# im_y = cv.filter2D(img_orig, cv.CV_64F, sobel_y)

fig, ax = plt.subplots (1, 2, figsize=(12, 6))
ax[0].imshow(im_x, cmap='gray')
ax[0].set_title('Sobel X (Using seperable filters)')  
ax[0].axis('off')
ax[1].imshow(im_y, cmap='gray')
ax[1].set_title('Sobel Y (Using seperable filters)')
ax[1].axis('off')

plt.show()