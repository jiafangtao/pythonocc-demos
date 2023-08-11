#
# Task 3: this script creates primitive geometry shapes.
#

from operator import add
from OCC.Core.BRepPrimAPI import (
    BRepPrimAPI_MakeBox,
    BRepPrimAPI_MakeCylinder,
    BRepPrimAPI_MakeWedge,
    BRepPrimAPI_MakeSphere,
    BRepPrimAPI_MakeTorus,
)
from OCC.Display.SimpleGui import init_display
from OCC.Core.gp import gp_Ax1, gp_Pnt, gp_Dir, gp_Trsf, gp_Vec
from OCC.Core.TopLoc import TopLoc_Location


shape_holder = dict()

def printLoc(loc, prefix=None):
    if loc:
        msg = loc.DumpJsonToString()
        print(f"{prefix}: {msg}")

def create_a_box(event=None):

    global shape_holder
    box = BRepPrimAPI_MakeBox(10.0, 10.0, 10.0).Shape()
    shape_holder['box'] = box

    ais_box = display.DisplayShape(box)[0]
    shape_holder["ais_box"] = ais_box
    display.FitAll()

def create_a_sphere(event=None):
    sphere = BRepPrimAPI_MakeSphere(5.0).Shape()

    global shape_holder
    ais_sphere = display.DisplayShape(sphere)[0]
    shape_holder["sphere"] = ais_sphere
    display.FitAll()

def create_a_cylinder(event=None):
    cylinder = BRepPrimAPI_MakeCylinder(5.0, 10.0).Shape()
    
    global shape_holder
    ais_cylinder = display.DisplayShape(cylinder)[0]
    shape_holder["cylinder"] = ais_cylinder
    display.FitAll()

def location_increase_x(event=None):
    global shape_holder
    box = shape_holder.get('box')
    ais_shape = shape_holder.get("ais_box")
    if ais_shape is not None:
        loc = display.Context.Location(ais_shape)
        #printLoc(loc, "Context.Location")

        aCubeTrsf = gp_Trsf()
        #aCubeTrsf.SetTranslation(gp_Pnt(0, 0, 0), gp_Pnt(10, 0, 0))
        aCubeTrsf.SetTranslation(gp_Vec(10, 0, 0))
        aCubeToploc = TopLoc_Location(aCubeTrsf)
        #box.Move(aCubeToploc)
        new_box = box.Moved(aCubeToploc)
        #display.DisplayShape(new_box)
                
        # clean previous AIS shape off screen
        display.Context.Erase(ais_shape, True)
        ais_shape = display.DisplayShape(new_box)[0]
        shape_holder['ais_box'] = ais_shape
        #display.Context.SetLocation(ais_shape, aCubeToploc)
        #printLoc(aCubeToploc, "context >>>")

        # clean old topo objects
        box.Nullify()
        box = new_box
        shape_holder['box'] = box

        printLoc(box.Location(), "box")
        #display.FitAll()
        
        display.Context.UpdateCurrentViewer()

def location_increase_y(event=None):
    pass

def location_increase_z(event=None):
    global shape_holder
    ais_shape = shape_holder.get("box")
    if ais_shape is not None:
        loc = display.Context.Location(ais_shape)
        print(loc)

        aCubeTrsf = gp_Trsf()
        #aCubeTrsf.SetRotation(ax1, angle)
        aCubeTrsf.SetTranslation(gp_Pnt(0, 0, 0), gp_Pnt(0, 0, 5))
        aCubeToploc = TopLoc_Location(aCubeTrsf)
        display.Context.SetLocation(ais_shape, aCubeToploc)
        loc = display.Context.Location(ais_shape)
        print(loc)

        display.Context.UpdateCurrentViewer()

def location_decrease_x(event=None):
    global shape_holder
    ais_shape = shape_holder.get("box")
    if ais_shape is not None:
        loc = display.Context.Location(ais_shape)
        print(loc)

        aCubeTrsf = gp_Trsf()
        #aCubeTrsf.SetRotation(ax1, angle)
        aCubeTrsf.SetTranslation(gp_Pnt(0, 0, 0), gp_Pnt(-10, 0, 0))
        aCubeToploc = TopLoc_Location(aCubeTrsf)
        display.Context.SetLocation(ais_shape, aCubeToploc)
        loc = display.Context.Location(ais_shape)
        print(loc)

        display.Context.UpdateCurrentViewer()


def location_decrease_y(event=None):
    pass

def location_decrease_z(event=None):
    global shape_holder
    ais_shape = shape_holder.get("box")
    if ais_shape is not None:
        aCubeTrsf = gp_Trsf()
        #aCubeTrsf.SetRotation(ax1, angle)
        aCubeTrsf.SetTranslation(gp_Pnt(0, 0, 0), gp_Pnt(0, 0, -5))
        aCubeToploc = TopLoc_Location(aCubeTrsf)
        display.Context.SetLocation(ais_shape, aCubeToploc)
        loc = display.Context.Location(ais_shape)
        print(loc)

        display.Context.UpdateCurrentViewer()

def size_increase(event=None):
    pass

def size_decrease(event=None):
    pass

def rotation_clock_wise(event=None):
    pass

def rotation_anti_clock_wise(event=None):
    pass

def display_mode_shaded(event=None):
    display.Context.SetDisplayMode(1, True)

def display_mode_wireframe(event=None):
    display.Context.SetDisplayMode(0, True)

def clean_all(event=None):
    display.EraseAll()
    global shape_holder
    shape_holder = dict()

#
# views
#
def view_front(event=None):
    display.View_Front()

def view_left(event=None):
    display.View_Left()


if __name__ == "__main__":

    display, start_display, add_menu, add_function_to_menu = init_display()
    add_menu("Shapes")
    add_function_to_menu("Shapes", create_a_box)
    add_function_to_menu("Shapes", create_a_sphere)
    add_function_to_menu("Shapes", create_a_cylinder)

    add_menu("View")
    add_function_to_menu("View", view_front)
    add_function_to_menu("View", view_left)

    add_menu("Location")
    add_function_to_menu("Location", location_increase_x)
    add_function_to_menu("Location", location_increase_y)
    add_function_to_menu("Location", location_increase_z)
    add_function_to_menu("Location", location_decrease_x)
    add_function_to_menu("Location", location_decrease_y)
    add_function_to_menu("Location", location_decrease_z)

    add_menu("Size")
    add_function_to_menu("Size", size_increase)
    add_function_to_menu("Size", size_decrease)

    add_menu("Rotation")
    add_function_to_menu("Rotation", rotation_clock_wise)
    add_function_to_menu("Rotation", rotation_anti_clock_wise)

    add_menu("Mode")
    add_function_to_menu("Mode", display_mode_shaded)
    add_function_to_menu("Mode", display_mode_wireframe)

    add_menu("Others")
    add_function_to_menu("Others", clean_all)

    start_display()
