import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img_orig = cv.imread('a1images/daisy.jpg')

mask = np.zeros(img_orig.shape[:2], np.uint8)
