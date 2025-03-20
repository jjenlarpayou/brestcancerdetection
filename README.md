# Brestcancerdetection

## Overview
This group project is Detection of Region of Interests (RoIs) of Breast Cancer Biopsy using Deep Learning. The research is inspired by the application of U-Net to segment ROIs in WSIs of invasive breast cancer. Given the visual and structural similarities between the WSIs and the images in the BRACS dataset, the U-Net model is exceptionally well-suited for this project.

## Dataset
The dataset can be downloaded from https://www.bracs.icar.cnr.it

### Whole Slide Image Set
WSIs are stored as multi-resolution pyramid structures in the .svs file format, with the highest resolution images sometimes exceeding dimensions of 100,000 by 100,000 pixels. Some WSIs also come with .qpdata files of the same name, allowing for viewing annotations within the WSI(Brancati et al., 2022).

### Regions of Interest  Set
ROIs are provided in .png format, with each filename containing the corresponding WSI name and ROI subtype (e.g., BRACS_010_PB_32.png represents ROI 32 from WSI BRACS_010.svs, categorized as Pathological Benign). ROIs are 40× in dimension, often exceeding 4,000 by 4,000 pixels(Brancati et al., 2022).

## Prequities

