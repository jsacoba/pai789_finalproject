# 1. Import modules.

import pandas as pd
import geopandas

# 2. Read '"TM_WORLD_BORDERS-0.3.gpkg"' file.

tm = geopandas.read_file("TM_WORLD_BORDERS-0.3.gpkg")

# 3. Fix `bytes` issue for '"Åland Island"'.

tm['name'] = tm['name'].where( tm['iso2'] != 'AX', "Åland Island" )

# 4. Save 'tm' as '"TM_WORLD_BORDERS-0.3-fixed.gpkg"'

tm.to_file("TM_WORLD_BORDERS-0.3-fixed.gpkg",driver="GPKG")

# 5. Read 'combined_clean.csv'.

geo_csv = pd.read_csv('combined_clean.csv')

# 6. Read '"TM_WORLD_BORDERS-0.3-fixed.gpkg"'.

geo_zip = geopandas.read_file("TM_WORLD_BORDERS-0.3-fixed.gpkg")

# 7. Join the data sets.

joined = geo_zip.merge(geo_csv, on='iso3', how = 'left', 
                       validate = '1:1', indicator = True )

# 8. Print 'value_counts', then drop '_merge' column from 'joined'.

print(joined['_merge'].value_counts())
joined = joined.drop('_merge', axis= 1)

# 9. Write out `joined` to a geopackage file called `"world.gpkg"`. 
#    Set the layer to `"2020"` and specify `driver="GPKG"`.

joined.to_file("world.gpkg", layer = "2020", driver = "GPKG")

