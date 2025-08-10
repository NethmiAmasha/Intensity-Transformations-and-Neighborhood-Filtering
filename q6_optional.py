import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/jeniffer.jpg')
img_hsv = cv.cvtColor(img_orig, cv.COLOR_BGR2HSV)
h, s, v = cv.split(img_hsv)

_, mask = cv.threshold(s, 13, 255, cv.THRESH_BINARY)  # Apply thesholding to saturation plane
foreground = cv.bitwise_and(img_orig, img_orig, mask=mask)  # Extract foreground using mask
background = cv.bitwise_and(img_orig, img_orig, mask=cv.bitwise_not(mask))  # Extract background

v_foreground = v[mask > 0]  # Extract value plane of foreground
hist, bins = np.histogram(v_foreground.ravel(), 256, [0, 256])  # Histogram of value plane
cdf = hist.cumsum()  # Cumulative distribution function
L = 256
MN = v_foreground.size
t = np.array([(L-1) / (MN) * cdf[i] for i in range(256)]).astype('uint8')
v_foreground_eq = v.copy()
v_foreground_eq[mask > 0] = t[v_foreground]
foreground_eq = cv.merge((h, s, v_foreground_eq))
foreground_eq = cv.cvtColor(foreground_eq, cv.COLOR_HSV2BGR)  # Convert back to BGR color space
foreground_eq = cv.bitwise_and(foreground_eq, foreground_eq, mask=mask)  # Ensure foreground_eq is masked
img_modified = cv.add(foreground_eq, background)  # Combine modified foreground with background

fig, axis = plt.subplots(1, 3, figsize=(12, 8))
axis[0].imshow(mask, cmap='gray')
axis[0].set_title('Foreground Mask')
axis[1].imshow(cv.cvtColor(img_orig, cv.COLOR_BGR2RGB))
axis[1].set_title('Original Image')
axis[2].imshow(cv.cvtColor(img_modified, cv.COLOR_BGR2RGB))
axis[2].set_title('Modified Image with Equalized Foreground')
for i in axis:
    i.axis('off')


# ----- Plotting the histrograms of the value plane -----

# hist_eq, bins_eq = np.histogram(v_foreground_eq[mask > 0].ravel(), 256, [0, 256])
# fig, ax = plt.subplots(1, 2, figsize=(12, 4))
# ax[0].plot(hist)
# ax[0].set_title('Histogram of Value Plane of Foreground')
# ax[0].set_xlabel('Intensity Value')
# ax[0].set_ylabel('Frequency')
# ax[1].plot(hist_eq)
# ax[1].set_title('Histogram of Equalized Value Plane of Foreground')
# ax[1].set_xlabel('Intensity Value') 
# ax[1].set_ylabel('Frequency')


# ----- Plotting the foreground -----

# fig, ax = plt.subplots(1, 1, figsize=(12, 4))
# ax.imshow(cv.cvtColor(foreground, cv.COLOR_BGR2RGB))
# ax.axis('off')


# ----- Plotting the 3 planes of HSV -----

# fig, ax = plt.subplots(1, 3, figsize=(12,4))
# ax[0].imshow(h, cmap='gray')
# ax[0].set_title('Hue')
# ax[1].imshow(s, cmap='gray')
# ax[1].set_title('Saturation')
# ax[2].imshow(v, cmap='gray')
# ax[2].set_title('Value')
# for i in ax:
#     i.axis('off')
plt.show()