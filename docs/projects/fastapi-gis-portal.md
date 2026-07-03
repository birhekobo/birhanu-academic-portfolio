---
title: FastAPI GIS Portal
parent: Projects
---

# FastAPI GIS Portal

## Overview

A RESTful API for serving and analyzing geospatial data, built with FastAPI and PostGIS.

## Objectives

- Expose geospatial data via standard REST endpoints
- Support vector and raster data operations
- Provide spatial query capabilities (intersection, buffer, clipping)
- Deliver OGC-compliant services (WMS, WFS)

## API endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/layers` | GET | List available geospatial layers |
| `/api/layers/{id}` | GET | Get layer metadata |
| `/api/layers/{id}/query` | POST | Spatial query within AOI |
| `/api/layers/{id}/stats` | GET | Zonal statistics |
| `/api/export` | POST | Export data to GeoJSON, Shapefile, GeoTIFF |

## Links

```{grid} 3
:gutter: 2

```{grid-item-card} 💻 Code
:link: https://github.com/birhekobo/fastapi-gis-portal
```

```{grid-item-card} 📖 Docs
:link: https://fastapi-gis-portal.readthedocs.io
```

```{grid-item-card} 🎮 Demo
:link: https://fastapi-gis-portal.herokuapp.com/docs
```
```
