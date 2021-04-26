import pandas as pd
import geopandas

#https://www.igismap.com/download-world-shapefile-free-country-borders-continents/

geo_csv = pd.read_csv('plots_data.csv')

geo_zip = geopandas.read_file("TM_WORLD_BORDERS-0.3.gpkg")

joined = geo_zip.merge(geo_csv, on='iso3', how = 'left', 
                       validate = '1:1', indicator = True )

print(joined['_merge'].value_counts())

joined = joined.drop('_merge', axis= 1)

# Write out `geodata` to a geopackage file called `"counties.gpkg"`. 
# Set the layer to `"earnings"` and specify `driver="GPKG"`.

joined.to_file("world.gpkg", layer = "2020", driver = "GPKG")

