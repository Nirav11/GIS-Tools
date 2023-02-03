# Import arcpy module
import os
import fnmatch
from arcpy import env

rootdir = 'D:/test/attest/'
road = 'D:/test/attest/Road/Bandipur_Road.shp'
arcpy.MakeFeatureLayer_management(road)
mdb = []

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.shp'):
			mdb.append(os.path.join(subdir, file))

print(mdb)
# Set local variables
fieldName1 = "Areasqm"
fieldName2 = "LandUse"

fieldLength = 20

# Set Calculate geometry variables
expression = "SQUARE_METERS"
exp1 = "!SHAPE.AREA@SQUAREMETERS!"
query = "\"Shape_Area\" < 5000"


# Run calculate geometry
for i in range(len(mdb)):
    shpfile = mdb[i]
    arcpy.env.workspace = mdb[i]
    shapefile = arcpy.MakeFeatureLayer_management(shpfile)
    print(shpfile)
    arcpy.AddField_management(shpfile, fieldName1, 'DOUBLE', 
                          field_length=fieldLength)
    arcpy.AddField_management(shpfile, fieldName2, 'TEXT', 
                          field_length=fieldLength)

    arcpy.CalculateField_management(shpfile, 'Areasqm', exp1 ,'PYTHON')
    inter1 = arcpy.SelectLayerByLocation_management(shapefile, "WITHIN_A_DISTANCE", road, "1 Meters", "ADD_TO_SELECTION", "NOT_INVERT")
    # inter2 = arcpy.MakeFeatureLayer_management(inter1)
    # inter3 = arcpy.SelectLayerByAttribute_management(inter1, "SUBSET_SELECTION", "\"Shape_Area\" < 5000")
    inter3 = arcpy.SelectLayerByAttribute_management(inter1, "SUBSET_SELECTION", query)
    arcpy.CalculateField_management(inter3, 'LandUse', "\"Residential\"", "PYTHON")

    
 

