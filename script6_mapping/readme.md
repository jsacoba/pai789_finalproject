![Indices Map](https://github.com/jsacoba/pai789_finalproject/blob/main/script6_mapping/joined_maps.png)

# Script No. 5.4: Joining Data Using Geopandas and Creating Map using QGIS

## A. Summary

This script uses `pandas`, and `geopandas` modules of `Python`. The script is aimed at creating a `.gpkg` file from the master file ***combined_clean.csv*** file to be used in mapping `EPI` and `WRI` in `QGIS`.

## B. Input Data

There are two input data in this script:

1. The master file ***combined_clean.csv*** we generated in `script4_combine` folder; and

2. A shapefile with filename ***TM_WORLD_BORDERS-0.3.gpkg*** downloaded from: `https://www.igismap.com/download-world-shapefile-free-country-borders-continents/`

## C. Deliverables

1. Script named ***riskmap_world.py***; and

2. Output geopackage file with name ***world.gpkg***.

## D. Instructions

1. Import `pandas` as `pd` and import `geopandas`.

2. Read input file by assigning `tm` to the result of calling `geopandas.readfile()` on `"TM_WORLD_BORDERS-0.3.gpkg"` as argument.

3. Fix `bytes` type for `"Åland Island"` by assigning the `"name"` column of `tm` to the result of calling `.where()` to the `"name"` column of `tm`, with arguments `tm['iso2'] != 'AX', "Åland Island"`. That is:

    `tm['name'] = tm['name'].where(tm['iso2'] != 'AX', "Åland Island")`

4. Save `tm` to file by calling `.to_file()` to `tm` with arguments `"TM_WORLD_BORDERS-0.3-fixed.gpkg",driver="GPKG`.

5. Assign `geo_csv` to the result of calling `pd.read-csv` to `combined_clean.csv`.

6. Assign `geo_zip` to the result of calling `geopandas.read_file()` with argument `"TM_WORLD_BORDERS-0.3-fixed.gpkg"`.

7. Do a one to one left join for the two data sets. Join `geo_csv` by calling `.merge()` onto `geo_zip` using `iso3` as join key. Add `indicator = True` in the argument.

8. Print the result of calling `.value_counts()` to the `_merge` column of `joined`, then drop `_merge` column from `joined`.

9. Write out `joined` to a geopackage file called `"world.gpkg"`. Set the layer to `"2020"` and specify `driver="GPKG"`.