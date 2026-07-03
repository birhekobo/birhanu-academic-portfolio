---
title: Earth Observation
parent: Research
---

# Earth Observation

## Overview

Integrating multi-sensor Earth observation data for comprehensive environmental monitoring. This research area focuses on data fusion, synergistic use of different sensors, and developing analysis-ready datasets.

## Sensor capabilities

| Sensor | Spectral bands | Resolution | Applications |
|--------|---------------|------------|--------------|
| Landsat 8/9 OLI | VNIR + SWIR + TIR | 30 m / 100 m | LULC, LST, change |
| Sentinel-2 MSI | VNIR + SWIR + red-edge | 10–60 m | Vegetation, agriculture |
| Sentinel-1 C-SAR | C-band | 10–40 m | Flood, wetland, deformation |
| MODIS | 36 bands | 250–1000 m | Global monitoring, phenology |
| VIIRS | 22 bands | 375–750 m | Nightlights, SST, AOD |
| ECOSTRESS | TIR | 70 m | Evapotranspiration |

## Data fusion approaches

- **Optical + SAR** — combining Sentinel-1 and Sentinel-2 for cloud-free composites
- **Multi-resolution fusion** — downscaling coarse-resolution data with fine-resolution imagery
- **Time series harmonization** — Landsat + Sentinel-2 combined ARD

## Applications

- Analysis Ready Data (ARD) pipelines
- Multi-sensor land cover mapping
- Fusion-based cloud removal
- High-resolution ET estimation
