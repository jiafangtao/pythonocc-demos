#
# Task 3: this script creates primitive geometry shapes.
#

from OCC.Core.BRepPrimAPI import (
    BRepPrimAPI_MakeBox,
    BRepPrimAPI_MakeCylinder,
    BRepPrimAPI_MakeWedge,
    BRepPrimAPI_MakeSphere,
    BRepPrimAPI_MakeTorus,
)
from OCC.Display.SimpleGui import init_display

def create_a_box(event=None):
    display.EraseAll()
    box = BRepPrimAPI_MakeBox(10.0, 10.0, 10.0).Shape()
    display.DisplayShape(box)
    display.FitAll()

def create_a_sphere(event=None):
    display.EraseAll()
    sphere = BRepPrimAPI_MakeSphere(50.0).Shape()
    display.DisplayShape(sphere)
    display.FitAll()

def create_a_cylinder(event=None):
    display.EraseAll()
    shape = BRepPrimAPI_MakeCylinder(50.0, 100.0).Shape()
    display.DisplayShape(shape)
    display.FitAll()


if __name__ == "__main__":

    display, start_display, add_menu, add_function_to_menu = init_display()
    add_menu("New Shapes")
    add_function_to_menu("New Shapes", create_a_box)
    add_function_to_menu("New Shapes", create_a_sphere)
    add_function_to_menu("New Shapes", create_a_cylinder)

    start_display()
