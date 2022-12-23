import os

base_dir  = 'F:/srs/'
input_dir = 'F:/srs/Input/'
join_dir  = 'F:/srs/Join/'

def merge_file(is_test=True):
    # loop over folder
    vdc_names = os.listdir(input_dir)
    
    if not is_test:
        import arcpy
        from arcpy import env
        env.workspace = base_dir

    for vdc_name in vdc_names:
        print vdc_name
        files  = os.listdir(input_dir+vdc_name)
        for file in files:
            try:
                if not file.endswith(".shp"): continue 
                # print file
                input_file = input_dir+vdc_name+"/"+file
                join_file  = join_dir+vdc_name+"/"+file
                if not os.path.exists(join_file):
                    print "NOT FOUND ", join_file 
                    print input_file,"  <-  ", join_file
                    if not is_test:
                        merge_shp_file(input_file, join_file)
                        
            except Exception as e:
                print str(e)
    return
    
def merge_shp_file(input_file, join_file ):
    arcpy.JoinField_management(
        input_file, 
        "PARCEL_NO", 
        join_file, "PARCELNO", 
        ""
    )


if __name__ == '__main__':
    # merge_file(is_test=True)
    merge_file(is_test=False)