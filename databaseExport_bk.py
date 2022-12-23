#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from osgeo import ogr
import gdal
import psycopg2

import subprocess


def discover_geom_name(ogr_type):
    """
    :param ogr_type: ogr GetGeomType()
    :return: string geometry type name
    """
    return {
        ogr.wkbUnknown              : "UNKNOWN",
        ogr.wkbPoint                : "POINT",
        ogr.wkbLineString           : "LINESTRING",
        ogr.wkbPolygon              : "POLYGON",
        ogr.wkbMultiPoint           : "MULTIPOINT",
        ogr.wkbMultiLineString      : "MULTILINESTRING",
        ogr.wkbMultiPolygon         : "MULTIPOLYGON",
        ogr.wkbGeometryCollection   : "GEOMETRYCOLLECTION",
        ogr.wkbNone                 : "NONE",
        ogr.wkbLinearRing           : "LINEARRING"}.get(ogr_type)
        

def run_shp2pg(input_shp):
    try:

        # print("Input Shapefile", input_shp)
        connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "localhost",
                                    port = "5432",
                                    database = "dudbc")
    
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    
    # print ("Connection ", connection)
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    # print ( connection.get_dsn_parameters(),"\n")


    db_schema = "SCHEMA = dudbc"
    db_connection = """PG:host=localhost port=5432 user=postgres
        dbname=dudbc password=postgres"""
    output_format ="PostgreSQL"
    overwrite_option = "OVERWRITE=YES"
    shp_dataset = shp_driver.Open(input_shp)
    # print("Shape Dataset:", shp_dataset)
    layer = shp_dataset.GetLayer()
    # print("Layer: ", layer)
    geometry_type = layer.GetLayerDefn().GetGeomType()
    geometry_name = discover_geom_name(geometry_type)
    # print ("Geometry Name",geometry_name)

    # ogr2ogr -lco db_schema -lco overwrite_option OVERWRITE=YES -nlt POINT -skipfailures -f PostgreSQL PG:host=localhost port=5432 user=postgres dbname=dudbc password=postgres C:\Users\SRSES\Desktop\Test\build_pt.shp
     
    try:

        subprocess.call(["ogr2ogr", "-lco", db_schema, "-lco", overwrite_option,
                            "-nlt", geometry_name,
                            "-f", output_format, db_connection, input_shp])
    except subprocess.CalledProcessError as e:
        print("Exception", e.output)

    finally:
        print("Successful!!")

# directory full of shapefiles
shapefile_dir = os.path.realpath('D:\\Test\\building')

# define the ogr spatial driver type
shp_driver = ogr.GetDriverByName('ESRI Shapefile')

# empty list to hold names of all shapefils in directory
shapefile_list = []

for shp_file in os.listdir(shapefile_dir):
    if shp_file.endswith(".shp"):
        # print("Shapefiles:", shp_file)
        # apped join path to file name to outpout "../geodata/myshape.shp"
        full_shapefile_path = os.path.join(shapefile_dir, shp_file)
        # print("Full path to Shapefile:" ,  full_shapefile_path)
        shapefile_list.append(full_shapefile_path)
    

# run_shp2pg(shapefile_list[0])
print("shapefile list:", shapefile_list, type(shapefile_list))

# loop over list of Shapefiles running our import function
for each_shapefile in shapefile_list:
    run_shp2pg(each_shapefile)
    # print ("importing Shapefile: "+ each_shapefile)
