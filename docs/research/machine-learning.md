---
title: Machine Learning
parent: Research
---

# Machine Learning

## Overview

Developing and applying machine learning and deep learning methods for geospatial and remote sensing data analysis.

## Approaches

```{list-table}
:header-rows: 1

* - Method
  - Application
  - Framework
* - Random forest
  - Land cover classification
  - scikit-learn, GEE
* - Support vector machines
  - Change detection
  - scikit-learn
* - Convolutional neural networks
  - Crop type mapping, object detection
  - PyTorch, TensorFlow
* - U-Net / DeepLab
  - Semantic segmentation of satellite imagery
  - PyTorch
* - LSTM
  - Time series prediction (NDVI, climate)
  - PyTorch
* - Autoencoders
  - Anomaly detection in EO data
  - PyTorch
```

## Current work

- **Crop type mapping** — CNN-based classification of Sentinel-2 time series
- **Land cover segmentation** — U-Net on high-resolution imagery
- **Drought prediction** — LSTM networks for multi-index drought forecasting
- **Change detection** — Siamese networks for bitemporal analysis

## Tools

- Python (PyTorch, TensorFlow, scikit-learn, xarray, rioxarray)
- Google Earth Engine (ML capabilities)
- R (caret, randomForest, keras)
- MLflow for experiment tracking
