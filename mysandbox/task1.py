#
# This task takes in a step file and shows it, as well offers exporting it as glTF format.
#

import random

from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_step_file
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Core.TDocStd import TDocStd_Document
from OCC.Core.TCollection import TCollection_AsciiString
from OCC.Core.TCollection import TCollection_ExtendedString
from OCC.Core.XCAFDoc import (
    XCAFDoc_DocumentTool_ShapeTool,
    XCAFDoc_DocumentTool_LayerTool,
)

from OCC.Core.TColStd import TColStd_IndexedDataMapOfStringString
from OCC.Core.Message import Message_ProgressRange
from OCC.Core.BRepMesh import BRepMesh_IncrementalMesh
from OCC.Core.BRepTools import breptools_Clean

# GLTF export
from OCC.Core.RWGltf import RWGltf_CafWriter, RWGltf_WriterTrsfFormat


def import_as_one_shape(event=None):
    global filename
    global shp
    
    shp = read_step_file(filename)
    print(shp)
    print(shp.TShape())
    display.EraseAll()
    display.DisplayShape(shp, update=True)


def import_as_multiple_shapes():
    global filename
    global shp

    compound = read_step_file(filename)
    t = TopologyExplorer(compound)
    display.EraseAll()
    for solid in t.solids():
        color = Quantity_Color(
            random.random(), random.random(), random.random(), Quantity_TOC_RGB
        )
        display.DisplayColoredShape(solid, color)
    display.FitAll()


def export_to_gltf(event=None):
    # create a document
    docname = TCollection_ExtendedString("dianzijixiang")

    doc = TDocStd_Document(docname)
    shape_tool = XCAFDoc_DocumentTool_ShapeTool(doc.Main())
    layer_tool = XCAFDoc_DocumentTool_LayerTool(doc.Main())

    # mesh shape
    global shp
    breptools_Clean(shp)

    #b2 = BRep_Builder()
    #b2.Add(shp)

    # Triangulate
    msh_algo = BRepMesh_IncrementalMesh(shp, True)
    msh_algo.Perform()

    sub_shape_label = shape_tool.AddShape(shp)

    # GLTF options
    a_format = RWGltf_WriterTrsfFormat.RWGltf_WriterTrsfFormat_Compact
    force_uv_export = True

    # metadata
    a_file_info = TColStd_IndexedDataMapOfStringString()
    a_file_info.Add(
        TCollection_AsciiString("Authors"), TCollection_AsciiString("brucejia")
    )

    #
    # Binary export
    #
    binary = True
    output_name = TCollection_AsciiString("box.glb")
    binary_rwgltf_writer = RWGltf_CafWriter(output_name, binary)
    binary_rwgltf_writer.SetTransformationFormat(a_format)
    binary_rwgltf_writer.SetForcedUVExport(force_uv_export)
    pr = Message_ProgressRange()  # this is required
    binary_rwgltf_writer.Perform(doc, a_file_info, pr)

    #
    # Ascii export
    #
    binary = False
    output_name = TCollection_AsciiString("box.gltf")
    ascii_rwgltf_writer = RWGltf_CafWriter(output_name, binary)
    ascii_rwgltf_writer.SetTransformationFormat(a_format)
    ascii_rwgltf_writer.SetForcedUVExport(force_uv_export)
    pr = Message_ProgressRange()  # this is required
    ascii_rwgltf_writer.Perform(doc, a_file_info, pr)


if __name__ == "__main__":

    # globals
    filename = "dianzijixiang.stp"
    shp = None

    display, start_display, add_menu, add_function_to_menu = init_display()
    add_menu("STEP import")
    add_function_to_menu("STEP import", import_as_one_shape)
    add_function_to_menu("STEP import", import_as_multiple_shapes)

    add_menu("Export")
    add_function_to_menu("Export", export_to_gltf)

    start_display()
