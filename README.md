# Brestcancerdetection

## Overview
This group project is Detection of Region of Interests (RoIs) of Breast Cancer Biopsy using Deep Learning. The research is inspired by the application of U-Net to segment ROIs in WSIs of invasive breast cancer. Given the visual and structural similarities between the WSIs and the images in the BRACS dataset, the U-Net model is exceptionally well-suited for this project.

## Dataset
The dataset can be downloaded from https://www.bracs.icar.cnr.it

- 547 whole slide images (WSIs) with 4539
regions of interests (ROIs)
- The ROIs include 7 categories annotated by
3 pathologists
- Each whole slide images include 100,000 x
90,000 pixels (~2-3GB each)
- Initial task: identify two biologically relevant
regions UDH (Usual Ductal Hyperplasia)
and DCIS (Atypical Ductal Hyperplasia)
which are differ by the severity of the cancer

### Whole Slide Image Set
WSIs are stored as multi-resolution pyramid structures in the .svs file format, with the highest resolution images sometimes exceeding dimensions of 100,000 by 100,000 pixels. Some WSIs also come with .qpdata files of the same name, allowing for viewing annotations within the WSI(Brancati et al., 2022).

### Regions of Interest  Set
ROIs are provided in .png format, with each filename containing the corresponding WSI name and ROI subtype (e.g., BRACS_010_PB_32.png represents ROI 32 from WSI BRACS_010.svs, categorized as Pathological Benign). ROIs are 40× in dimension, often exceeding 4,000 by 4,000 pixels(Brancati et al., 2022).

## Prerequisites
### **1. Required Software**
- **Python 3.x** ([Download Here](https://www.python.org/downloads/))
- **OpenSlide** (For handling whole-slide images)
- **PyTorch** (For deep learning computations)
- **OpenCV** (For image processing)
- **GeoPandas** (For geospatial data handling)
- **Matplotlib** (For data visualization)
- **NumPy** (For numerical computations)
- **Rasterio** (For rasterizing shapes)
- **Shapely** (For geometric operations)
- **QuPath** (For digital pathology image analysis)
- **PIL (Pillow)** (For image manipulation)
- **TQDM** (For progress tracking)
- **Dataclasses** (For structured data storage)
- **JSON** (For handling JSON data)

## Key Features
- Generating tiled and masked images
- Removing excess background
- Training U-net model on grayscale
- Model evaluation

### Model used
- U-net

## Result
###
<div align="center"><img width="700" alt="image" src="https://github.com/user-attachments/assets/be2ed522-4082-4c5a-a8da-956ed4c0c388" />
</div>
<div align="center"><b>Figure 1: </b></b>Generated Tile Images</div>

### Excessive background removal
<div align="center"><img width="600" alt="image" src="https://github.com/user-attachments/assets/4fe2ecd9-7cb6-427b-8a88-19ce535f0c7a" />
</div>
<div align="center"><b>Figure 2: </b>Excessive Background Removal via Standard Deviation Adjustment</div>

### Training model on grayscale
<div align="center"><img width="600" alt="image" src="https://github.com/user-attachments/assets/0378b370-775f-4c8d-8152-f810a2cfa908" />
</div>
<div align="center"><b>Figure 3: </b>The model was trained on grayscale with BCEWithLogitsLoss loss function, Adam optimizer with lr =1e-3 with 64 x 64 input size</div>

### Metrics
- Accuracy: 0.79
- Precision: 0.52
- Recall: 0.21
- F1-Score: 0.30

## My Contributions
- Processed grayscale RoIs and preprocessed WSI tiles
- Implemented grayscale U-Net model
- Built performance metric visualizations
- Developed custom dataset class and wrapper
- Created confusion matrix for evaluation

