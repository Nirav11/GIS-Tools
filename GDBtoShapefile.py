import arcpy, os

arcpy.env.workspace = r'H:\IUDP\Environment'
inws = arcpy.env.workspace
outws = r'D:\Output1\Kalika\Environment'

fgdb = arcpy.ListWorkspaces(workspace_type = "fileGDB")

counter = 1
for f in fgdb:
    # Define the output .mdb name
    name = os.path.basename(f).split(".")[0]
    
    # Create a new personal gdb (.mdb)
    arcpy.CreatePersonalGDB_management(outws, name)
    outgdb = os.path.join(outws, name + ".mdb")

    # Get the FC's in FDS and copy to .mdb
    arcpy.env.workspace = os.path.join(inws, f, "")
    fcs1 = arcpy.ListFeatureClasses()
    for fc in fcs1:
        arcpy.CopyFeatures_management(fc, os.path.join(outgdb, fc))

    # Get stand-alone FC's and copy to .mdb
    arcpy.env.workspace = os.path.join(inws, f, "URS")
    fcs2 = arcpy.ListFeatureClasses()
    # Make sure there are FC's in the FDS
    if fcs2 != None:
        for fc in fcs2:
            arcpy.CopyFeatures_management(fc, os.path.join(outgdb, fc))

    print "%s of %s workspaces converted" % (counter, len(fgdb))
    counter = counter + 1

print "Processing complete."