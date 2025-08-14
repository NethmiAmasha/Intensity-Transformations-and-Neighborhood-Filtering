# EN3160 - Intensity Transformations and Neighborhood Filtering

This repository focuses on Intensity Transformations and Neighborhood Filtering where it involves implementing various image processing techniques on a set of images. This was done as part of the module Image Processing and Machine Vision- EN3160.
## Table of Contents
1.  [Dependencies](#dependencies)
2.  [Tasks](#tasks)
    *  [Intensity Transformation](#intensity-transformation)
    *  [Accentuate Brain Matter](#accentuate-brain-matter)
    *  [Gamma Correction](#gamma-correction)
    *  [Vibrance Enhancement](#vibrance-enhancement)
    *  [Histogram Equalization](#histogram-equalization)
    *  [Foreground Histogram Equalization](#foreground-histogram-equalization)
    *  [Sobel Filtering](#sobel-filtering)
    *  [Image Zooming](#image-zooming)
    *  [Image Segmentation and Enhancement](#image-segmentation-and-enhancement)
3.  [Results](#results)

## Dependencies

This project requires the following Python libraries:
*   OpenCV
*   NumPy
*   Matplotlib

You can install them using pip:
```bash
pip install opencv-python numpy matplotlib
```

## Tasks

### Intensity Transformation
*   **Task:** Implement the piecewise linear intensity transformation on the provided image of Emma Watson.
*   **Files:** `q1.py`, `a1images/emma.jpg`

### Accentuate Brain Matter
*   **Task:** Apply a similar piecewise linear transformation to accentuate the white and gray matter in a brain proton density image. The transformations are shown as plots.
*   **Files:** `q2.py`, `q2_histogram.py`, `a1images/brain_proton_density_slice.jpg`

### Gamma Correction
*   **Task:** Apply gamma correction to the L plane of an image in the L*a*b* color space. The gamma value is adjusted, and histograms of the original and corrected images are shown.
*   **Files:** `q3.py`, `a1images/highlights_and_shadows.jpg`

### Vibrance Enhancement
*   **Task:** Increase the vibrance of a photograph by applying a given intensity transformation to the saturation plane. The process involves splitting the image into H, S, V planes, applying the transformation, and recombining them.
*   **Files:** `q4.py`, `a1images/spider.png`

### Histogram Equalization
*   **Task:** Write a custom function to perform histogram equalization on an image. The histograms before and after equalization are displayed.
*   **Files:** `q5.py`, `a1images/shells.tif`

### Foreground Histogram Equalization
*   **Task:** Apply histogram equalization only to the foreground of an image. This involves creating a mask, separating the foreground and background, equalizing the foreground, and then merging them back.
*   **Files:** `q6.py`, `q6_optional.py`, `a1images/jeniffer.jpg`

### Sobel Filtering
*   **Task:** Compute the gradient of an image using the Sobel operator in three different ways: using the `filter2D` function, writing custom code, and using the separability property of the Sobel kernel.
*   **Files:** `q7.py`, `q7_2.py`, `q7_3.py`, `a1images/einstein.jpg`

### Image Zooming
*   **Task:** Write a program to zoom images by a given factor using both nearest-neighbor and bilinear interpolation methods. The results are tested by comparing scaled-up small images with their original larger versions.
*   **Files:** `q8.py`, `a1images/a1q5images/im01small.png`, `a1images/a1q5images/im01.png`

### Image Segmentation and Enhancement
*   **Task:** Use the GrabCut algorithm to segment a flower image. Then, produce an enhanced image with a substantially blurred background.
*   **Files:** `q9.py`, `a1images/daisy.jpg`

## Results

All the output images, plots, and histograms can be found in the `/Results` directory.
