import os
import arcpy
rootdir = 'C:\Users\SRSES\Downloads\New folder\Database'
outfolder = 'C:\Users\SRSES\Downloads\New folder\Output'
path = []
path1 = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        path.append(os.path.join(subdir, file))

for i in range(len(path)):
	arcpy.env.workspace = path[i]
	print path[i]
	'''for root, dirnames, file in os.walk(arcpy.env.workspace):
		for f in fnmatch.filter(file, '*.mdb'):
			print f'''
	fcList = arcpy.ListFeatureClasses("*")
	print fcList
	for f in fcList:
		
		name = str(f)
		#print name
		if name == "Parcel":
			path1.append(path[i]+"\\" + name)
			print("Path 1",path1) 
a = []
b = []
c = []
for i in range(len(path1)):
        cursor = arcpy.da.SearchCursor(path1[i], ['VDC', 'GRIDS1', 'WARDNO'])
        for row in cursor:
		#print row
				#print len(row)
                a.append(row[0])
                b.append(row[1])
                c.append(row[2])
                d=[a,b,c]
                break
	#print d

	#print "The grid value is" + str(a)


outdirname = []
for i in range(0, len(path)):
    outdirname.append(str(path[i]))
     
for i in range(0, len(outdirname)):
	name = str(outdirname[i]).split("\\")[-1]
	name1 = name.split(".")[0]
	path = outfolder + "\\" + name1
	print("Name: ",name)
	if not(os.path.exists(path)):
		os.makedirs(outfolder + '\\' + name1)
     
shp = r"C:\Users\SRSES\Downloads\New folder\Thuloshapefile.shp"
'''for i in range(0, len(shapefile)):
    s1.append(shapefile[i].rsplit("\\",1)[1])
    print s1'''


arcpy.env.workspace = "C:\Users\SRSES\Downloads\New folder"

arcpy.MakeFeatureLayer_management ("Thuloshapefile.shp", "sourcelyr")

for i in range(0, len(a)):
	name = str(outdirname[i]).split("\\")[-1]
	name1 = name.split(".")[0]
	where_clause = "\"GRID_SH\" =" + "'" + str(b[i]) + "'" +  " AND"+ "\"VDC\" ="  + "'" + str(a[i])+ "'" + " AND"+ "\"WARD\" =" +"'" +  str(c[i])+"'" 
	print("Where Clause",where_clause)
	shp = arcpy.SelectLayerByAttribute_management ("sourcelyr", "NEW_SELECTION", where_clause)
	outlocation = outfolder + "\\" + name1+ ".shp"
	arcpy.CopyFeatures_management(shp, outlocation)



