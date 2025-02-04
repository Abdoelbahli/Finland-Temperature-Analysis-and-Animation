import xarray as xr

# Load the NetCDF file
data = xr.open_dataset('/Data/ERA5-Land-Finland.nc')

# Inspect the dataset
print("Dataset: ")
print(data)

# Extract temperature data (e.g., 2m temperature)
temperature = data['t2m']  # Adjust variable name if needed

# Convert Kelvin to Celsius (optional)
temperature_celsius = temperature - 273.15

# Save as GeoTIFF (optional)
temperature_celsius.rio.to_raster('/Data/temperature.tif')