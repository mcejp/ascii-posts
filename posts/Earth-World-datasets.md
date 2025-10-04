---
layout: post
render_with_liquid: false
date: 2025-10-04
title: "Earth/World datasets"
unlisted: true
---

## Digital Elevation Models (DEM)

### SRTMGL1

> SRTMGL1 (SRTM Global 1’’ arc second) is the historical DEM derived
> from the SRTM mission. The latest version v3 has been released on
> November 20th, 2013 and can be downloaded from the LPDAAC repository
> (<https://lpdaac.usgs.gov/products/srtmgl1v003/>). This global DEM
> extends is from 56° south to 60° north and covers about 80% of the
> land superficy. Its vertical datum is EGM96

> Version 3 (2013), also known as SRTM Plus, is void-filled with ASTER
> GDEM and USGS GMTED2010. This release is available in global
> 1-arcsecond (30 meter) resolution since 2014.

- Resolution: 1 arc-second (30 meters at equator)
- Tiling: 14296 tiles of 1x1 degree
- Format: zipped HGT
- Size: 88 GB in 14296 files

### NASADEM

> NASADEM is new processing of STRM data with several improvements
> (Crippen & al., 2016). Version 1 has been released on February 2020
> and it can be downloaded in its version 001 from the LPDAAC repository
> (<https://lpdaac.usgs.gov/products/nasadem_hgtv001/>)

- Resolution: 1 arc-second (30 meters at equator)
- Tiling: 14520 tiles of 1x1 degree
- Format: zipped HGT
- Size: 102 GB in 14520 files
- Download:
  <https://www.earthdata.nasa.gov/data/catalog/lpcloud-nasadem-hgt-001>
  (bulk download through Earthdata Search; free registration required)
- Online preview:
  <https://data.naturalcapitalproject.stanford.edu/dataset/sts-2b13519934614f4b36243eaeab5c712f37043413fb6fc314d588229a47808157>
- Press release:
  <https://www.earthdata.nasa.gov/about/competitive-programs/measures/new-nasa-digital-elevation-model>

### Other DEMs (unreviewed)

- [Sonny's LiDAR Digital Terrain Models of
  Europe](https://sonny.4lima.de/)
- [European Digital Elevation Model (EU-DEM)
  ](https://www.google.com/search?q=EU-DEM)

### Some Python libraries for DEM (unreviewed)

- <https://github.com/tkrajina/srtm.py>
- <https://pypi.org/search/?q=srtm>
- <https://pypi.org/project/NASADEM/>
- <https://pyrosar.readthedocs.io/en/latest/api/auxdata.html>

## Other Earth data

> Climate (rain & temperature) data is from The University of Delaware
> Center for Climatic Research's Climate Data Archive \[1\]
>
> Soil suborder data is from the USDA Natural Resources Conservation
> Service's Global Soil Region Map \[2\]
>
> \[1\] <http://climate.geog.udel.edu/~climate/html_pages/archive.html>
> \[2\]
> <https://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/use/?cid=nrcs142p2_054013>

#### MOD44W.061: MODIS/Terra Land Water Mask Derived from MODIS and SRTM L3 Global 250m SIN Grid V061

- Tiling: ?
- Size: 4.6 GiB in 7637 HDF4 files
- Download:
  <https://www.earthdata.nasa.gov/data/catalog/lpcloud-mod44w-061> (bulk
  download through Earthdata Search; free registration required)
- Older version on Google Earth Engine:
  <https://developers.google.com/earth-engine/datasets/catalog/MODIS_006_MOD44W>

#### ESA WorldCover v200 (10m)

- Format: Cloud Optimized GeoTIFF (COG)
- Tiling: 2651 tiles of 3x3 degrees
- Download: <https://worldcover2021.esa.int/downloader>
- Manual:
  <https://esa-worldcover.s3.eu-central-1.amazonaws.com/v200/2021/docs/WorldCover_PUM_V2.0.pdf>

#### Japanese city polygons

<https://github.com/tetunori/jpCityPolygon>

## Misc

[NASA Earthdata download script: patch to avoid re-downloading existing
files](https://gist.github.com/mcejp/54cf9dbac1647cd035164dbb931cb423)
