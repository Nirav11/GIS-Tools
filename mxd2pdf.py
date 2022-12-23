import arcpy, os

arcpy.env.workspace = ws = r"D:\Land Use\A1 map\PKG 34\CAPABILITY\SHEETWISE"

mxd_list = arcpy.ListFiles("*.mxd")

for mxd in mxd_list:
    current_mxd = arcpy.mapping.MapDocument(os.path.join(ws, mxd))
    pdf_name = mxd[:-4] + ".pdf"
    data_frame = 'PAGE_LAYOUT'
    resolution = "400"
    image_quality = "BEST"
    colorspace = "RGB"
    compress_vectors = "True"
    image_compression = "ADAPTIVE"
    picture_symbol = 'RASTERIZE_BITMAP'
    convert_markers = "TRUE"
    embed_fonts = "FALSE"
    layers_attributes = "LAYERS_ONLY"
    georef_info = "False"
    arcpy.mapping.ExportToPDF(current_mxd, pdf_name,data_frame, 640, 480, resolution, image_quality, colorspace, compress_vectors, image_compression, picture_symbol, convert_markers, embed_fonts, layers_attributes, georef_info)
 
del mxd_list
