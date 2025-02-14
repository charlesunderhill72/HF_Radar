#!/usr/bin/env python3

#
# GenerateDomainIndices.py - Takes lat and lon domain as input and returns index max and min for nc file.
# Made to be used with nc files that have a lat and lon coordinate. Returned indices can be used in 
# shell script to download subset of data from an OpenDAP archive.
#
# 11Jul24 Charles Underhill
#

import numpy as np
import xarray as xr
import sys

url = str(sys.argv[1])
lon = xr.open_dataset(url)["lon"]
lat = xr.open_dataset(url)["lat"]
lon0 = float(sys.argv[2])
lon1 = float(sys.argv[3])
lat0 = float(sys.argv[4])
lat1 = float(sys.argv[5])
lon_ind = np.where(np.logical_and(lon >= lon0, lon <= lon1))
lat_ind = np.where(np.logical_and(lat >= lat0, lat <= lat1))

print("url: ", url)
print(f"box: (lon0, lon1, lat0, lat1) = ({lon0}, {lon1}, {lat0}, {lat1})")
print(f"indices: ({lon_ind[0][0]}, {lon_ind[0][-1]}, {lat_ind[0][0]}, {lat_ind[0][-1]})")