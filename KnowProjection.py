import arcpy, os
import os

#from Tkinter import Tk
#from tkFileDialog import askdirectory
 
#Tk().withdraw() 
#filename = askdirectory()
#print(filename)

dir_name = "C:\\Users\\User\\Desktop\\GIS Data"
# dirs = [d for d in os.listdir(filename) if os.path.isdir(os.path.join(filename, d))]
# print(dirs)

for (current_dir, dirs,files) in os.walk(dir_name):
     arcpy.env.workspace = current_dir
     print(arcpy.env.workspace)
     for infc in arcpy.ListFeatureClasses():
          dsc = arcpy.Describe(infc)
          if dsc.spatialReference.Name == "Unknown":
               print('This fc has undefined coordinate system: ' + infc)
          else:
               print("Projection of {} is {}".format(infc,dsc.spatialReference.Name))
#        



#for i in range(0, len(dirs)):
#     in_workspace = filename+'/'+ dirs[i]
#     arcpy.env.workspace = in_workspace
#     print(arcpy.env.workspace)
#     for infc in arcpy.ListFeatureClasses():
#         dsc = arcpy.Describe(infc)
#         if dsc.spatialReference.Name == "Unknown":
#            print ('This fc has undefined coordinate system: ' + infc)
#         else:
#            print("Projection of {} is {}".format(infc,dsc.spatialReference.Name))
