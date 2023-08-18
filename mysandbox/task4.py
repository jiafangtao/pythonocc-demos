# Task 4:
#     1. open a stp file 
#     2. create a new box at a given position
#     3. save all shapes to a new stp file

import random

from OCC.Core.BRep import BRep_Builder
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeBox
from OCC.Core.gp import gp_Pnt
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Core.TopoDS import TopoDS_Compound
from OCC.Display.SimpleGui import init_display
from OCC.Extend.DataExchange import read_step_file
from OCC.Extend.TopologyUtils import TopologyExplorer

from OCC.Core.STEPControl import STEPControl_Writer, STEPControl_AsIs
from OCC.Core.Interface import Interface_Static_SetCVal
from OCC.Core.IFSelect import IFSelect_RetDone



def import_stp_file(filename, displayContext):
    compound = read_step_file(filename)
    t = TopologyExplorer(compound)
    displayContext.EraseAll()
    for solid in t.solids():
        color = Quantity_Color(
            random.random(), random.random(), random.random(), Quantity_TOC_RGB
        )
        displayContext.DisplayColoredShape(solid, color)
    displayContext.FitAll()
    return compound


def create_a_box(loc, dx, dy, dz):
	"""Create a box at given location, with specified width, height and thickness"""
	pt = gp_Pnt(loc['x'], loc['y'], loc['z'])
	box = BRepPrimAPI_MakeBox(pt, dx, dy, dz).Shape()
	return box


def save_stp_file(filename, shape):
	"""Save the shape into a stp file"""

	# initialize the STEP exporter
	step_writer = STEPControl_Writer()
	step_writer.WS().TransferWriter().FinderProcess()

	Interface_Static_SetCVal("write.step.schema", "AP203")

	# transfer shapes and write file
	step_writer.Transfer(shape, STEPControl_AsIs)
	status = step_writer.Write(filename)

	if status != IFSelect_RetDone:
	    raise AssertionError("load failed")


def main(displayContext):
	filename = "dianzijixiang.stp"
	compound = import_stp_file(filename, displayContext)

	loc = { 'x': 10.0, 'y': -68.0, 'z': 0.0}
	dx = 10
	dy = 8
	dz = 4
	box = create_a_box(loc, dx, dy, dz)

	# assemble all the parts
	aBuilder = BRep_Builder()
	result = TopoDS_Compound()

	aBuilder.MakeCompound(result)
	aBuilder.Add(result, box)
	aBuilder.Add(result, compound)
	displayContext.DisplayShape(result, update=True)

	save_stp_file("output.stp", result)


if __name__ == '__main__':
	# TODO: parse inputs like file name, location, dimensions, etc.

	display, start_display, add_menu, add_function_to_menu = init_display()
	main(displayContext=display)
	start_display()
