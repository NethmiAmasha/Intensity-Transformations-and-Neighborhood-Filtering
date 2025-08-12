import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/daisy.jpg')

mask = np.zeros(img_orig.shape[:2], np.uint8)
bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 130, 510, 450) # Adjusted to fit the daisy
cv.grabCut(img_orig, mask, rect, bgd_model, fgd_model, 5, cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
foreground = img_orig * mask2[:, :, np.newaxis]
background = img_orig * (1 - mask2[:, :, np.newaxis])

background_blurred = cv.GaussianBlur(background, (15, 15), 0)
img_enhanced = foreground + background_blurred * (1 - mask2[:, :, np.newaxis])

fig, ax = plt.subplots(1, 5, figsize=(15, 5))
ax[0].imshow(mask2, cmap='gray')
ax[0].set_title('Final Segmentation Mask')
ax[1].imshow(cv.cvtColor(foreground, cv.COLOR_BGR2RGB))
ax[1].set_title('Foreground')
ax[2].imshow(cv.cvtColor(background, cv.COLOR_BGR2RGB))
ax[2].set_title('Background')
ax[3].imshow(cv.cvtColor(img_orig, cv.COLOR_BGR2RGB))
ax[3].set_title('Original Image')
ax[4].imshow(cv.cvtColor(img_enhanced, cv.COLOR_BGR2RGB))
ax[4].set_title('Enhanced Image')
for a in ax:
    a.axis('off')

plt.show()