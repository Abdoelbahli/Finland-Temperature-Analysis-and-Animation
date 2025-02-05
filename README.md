# Finland Temperature Analysis & Animation

This project processes temperature data over Finland using ERA5-Land Climate Reanalysis data. The workflow includes:

1. **Data Transformation**  
   - Loading and converting ERA5-Land NetCDF data.
   - Saving the processed temperature data as a GeoTIFF file.

2. **Data Clipping**  
   - Clipping the temperature GeoTIFF to the boundaries of Finland using a shapefile.

3. **Visualization**  
   - Generating a series of PNG frames showing the monthly temperature variations.
   - Creating an animated GIF from the frames.

## Folder Structure

```markdown
my_project_root/
├── data/
│   ├── ERA5-Land-Finland.nc         # Original NetCDF dataset
│   ├── temperature.tif              # GeoTIFF produced from NetCDF data
│   ├── clipped_temperature.tif      # Temperature GeoTIFF clipped to Finland boundaries
│   └── fi_shp/                      # Finland shapefile folder
│       ├── fi.dbf
│       ├── fi.prj
│       ├── fi.shp
│       └── fi.shx
├── transform.py                 # Script to convert NetCDF to GeoTIFF
├── tem_analysis.ipynb           # Jupyter Notebook for clipping, processing, and animation
├── temperature_animation.gif    # Output animated GIF
└── temp_images/                 # Folder containing individual frame PNG images
    ├── frame_001.png
    ├── frame_002.png
    ├── frame_003.png
    └── ... (up to frame_252.png)
```

## Prerequisites

Make sure you have Python 3.7 or later installed. The project uses several Python packages for geospatial data handling and visualization.

## Installation

1. **Clone the repository** (if applicable) or download the project files.
2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Transform the NetCDF Data to GeoTIFF**  
   Run the `transform.py` script to load the ERA5-Land NetCDF file and create the `temperature.tif` file.
   
   ```bash
   python transform.py
   ```

2. **Clip the Temperature Data to Finland**  
   Open and run the cells in the Jupyter Notebook `tem_analysis.ipynb`. The notebook will:
   - Load and display the Finland shapefile.
   - Clip the `temperature.tif` using the Finland boundaries (producing `clipped_temperature.tif`).
   - Process each time step to create PNG frames in the `temp_images/` folder.
   - Assemble the frames into an animated GIF named `temperature_animation.gif`.

3. **View the Results**  
   - The clipped temperature GeoTIFF is saved in the `data/` folder.
   - The animated GIF is saved in the `transforming/` folder.

## Dependencies

The project relies on the following libraries:
- **xarray** and **rioxarray** for handling NetCDF data and exporting GeoTIFF files.
- **rasterio** for working with raster data.
- **geopandas** for handling shapefiles.
- **matplotlib** for visualization.
- **pandas** for date handling.
- **imageio** and **Pillow** for image processing and GIF creation.
- **numpy** for numerical operations.

For detailed package versions, please see the [requirements.txt](requirements.txt) file.


## Contact

For any questions or issues, please contact me.
