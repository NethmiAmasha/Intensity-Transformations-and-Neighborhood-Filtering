import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/shells.tif', cv.IMREAD_GRAYSCALE)

M, N = img_orig.shape
L = 256
hist_orig, bins_orig = np.histogram(img_orig.ravel(), 256, [0, 256])
cdf = hist_orig.cumsum()  # Cumulative distribution function
t = np.array([(L-1) / (M*N) * cdf[i] for i in range(256)]).astype('uint8')  # Transformation function
img_eq = cv.LUT(img_orig, t)  
hist_eq, bins_eq = np.histogram(img_eq.ravel(), 256, [0, 256])

fig, ax = plt.subplots(2, 2, figsize=(12, 4))
ax[0,0].imshow(img_orig, cmap='gray', vmin=0, vmax=255)
ax[0,0].set_title('Original Image')
ax[0,1].imshow(img_eq, cmap='gray', vmin=0, vmax=255)
ax[0,1].set_title('Equalized Image')
ax[1,0].plot(hist_orig)
ax[1,0].set_title('Histogram of Original Image')
ax[1,1].plot(hist_eq)
ax[1,1].set_title('Histogram of Equalized Image')
for i in ax[0, :]:
    i.axis('off')

plt.show()