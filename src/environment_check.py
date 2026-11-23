import sys
import geopandas as gpd
import rasterio
import xarray as xr
import sklearn
import duckdb

print("CHENNAI GEOSPATIAL PROJECT")
print("-------------------------")

print("Python:", sys.version)
print("GeoPandas:", gpd.__version__)
print("Rasterio:", rasterio.__version__)
print("Xarray:", xr.__version__)
print("Scikit-learn:", sklearn.__version__)
print("DuckDB:", duckdb.__version__)

print("\nGeospatial environment ready!")