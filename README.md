# EN3160 - Intensity Transformations and Neighborhood Filtering

This repository contains the solutions for the EN3160 Assignment 1, focusing on Intensity Transformations and Neighborhood Filtering. The assignment involves implementing various image processing techniques on a set of provided images.

## Table of Contents

1.  [Question 1: Intensity Transformation](#question-1-intensity-transformation)
2.  [Question 2: Accentuate Brain Matter](#question-2-accentuate-brain-matter)
3.  [Question 3: Gamma Correction](#question-3-gamma-correction)
4.  [Question 4: Vibrance Enhancement](#question-4-vibrance-enhancement)
5.  [Question 5: Histogram Equalization](#question-5-histogram-equalization) [
6.  [Question 6: Foreground Histogram Equalization](#question-6-foreground-histogram-equalization)
7.  [Question 7: Sobel Filtering](#question-7-sobel-filtering)
8.  [Question 8: Image Zooming](#question-8-image-zooming)
9.  [Question 9: Image Segmentation and Enhancement](#question-9-image-segmentation-and-enhancement)
10. [Results](#results)

## Project Structure

```
.
├── code
│   ├── question_1.py
│   ├── question_2.py
│   ├── question_3.py
│   ├── question_4.py
│   ├── question_5.py
│   ├── question_6.py
│   ├── question_7.py
│   ├── question_8.py
│   └── question_9.py
├── images
│   ├── emma_watson.jpg
│   ├── brain_proton_density.png
│   ├── gamma_correction_original.jpg
│   ├── vibrance_enhancement_original.jpg
│   ├── histogram_equalization_original.jpg
│   ├── foreground_equalization_original.jpg
│   ├── sobel_filtering_original.jpg
│   └── image_enhancement_original.jpg
├── results
│   ├── q1_output.png
│   ├── q2_white_matter_plot.png
│   ├── q2_gray_matter_plot.png
│   ├── ... (and so on for all results)
└── README.md
```

## Dependencies

This project requires the following Python libraries:
*   OpenCV (`opencv-python`)
*   NumPy
*   Matplotlib

You can install them using pip:
```bash
pip install opencv-python numpy matplotlib
```

## Assignment Questions

### Question 1: Intensity Transformation
*   **Task:** Implement the piecewise linear intensity transformation depicted in the assignment on the provided image of Emma Watson.
*   **Files:** `code/question_1.py`, `images/emma_watson.jpg`

### Question 2: Accentuate Brain Matter
*   **Task:** Apply a similar piecewise linear transformation to accentuate the white and gray matter in a brain proton density image. The transformations are shown as plots.
*   **Files:** `code/question_2.py`, `images/brain_proton_density.png`

### Question 3: Gamma Correction
*   **Task:** Apply gamma correction to the L plane of an image in the L*a*b* color space. The gamma value is stated, and histograms of the original and corrected images are shown.
*   **Files:** `code/question_3.py`, `images/gamma_correction_original.jpg`

### Question 4: Vibrance Enhancement
*   **Task:** Increase the vibrance of a photograph by applying a given intensity transformation to the saturation plane. The process involves splitting the image into H, S, V planes, applying the transformation, and recombining them.
*   **Files:** `code/question_4.py`, `images/vibrance_enhancement_original.jpg`

### Question 5: Histogram Equalization
*   **Task:** Write a custom function to perform histogram equalization on an image. The histograms before and after equalization are displayed.
*   **Files:** `code/question_5.py`, `images/histogram_equalization_original.jpg`

### Question 6: Foreground Histogram Equalization
*   **Task:** Apply histogram equalization only to the foreground of an image. This involves creating a mask, separating the foreground and background, equalizing the foreground, and then merging them back.
*   **Files:** `code/question_6.py`, `images/foreground_equalization_original.jpg`

### Question 7: Sobel Filtering
*   **Task:** Compute the gradient of an image using the Sobel operator in three different ways: using the `filter2D` function, writing custom code, and using the separability property of the Sobel kernel.
*   **Files:** `code/question_7.py`, `images/sobel_filtering_original.jpg`

### Question 8: Image Zooming
*   **Task:** Write a program to zoom images by a given factor using both nearest-neighbor and bilinear interpolation methods. The results are tested by comparing scaled-up small images with their original larger versions.
*   **Files:** `code/question_8.py`

### Question 9: Image Segmentation and Enhancement
*   **Task:** Use the GrabCut algorithm to segment a flower image. Then, produce an enhanced image with a substantially blurred background. An explanation for the dark edges around the flower in the enhanced image is also provided.
*   **Files:** `code/question_9.py`, `images/image_enhancement_original.jpg`

## Results

All the output images, plots, and histograms can be found in the `/results` directory. The report, which includes a detailed discussion of the results, is also available.
