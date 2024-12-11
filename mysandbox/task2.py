#! /usr/bin/env python3

#
# Task 2: dump a stp file
#

from OCC.Extend.DataExchange import read_step_file
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Extend.DataExchange import read_step_file


def main():
    pass

def import_as_multiple_shapes(filename: str):
    compound = read_step_file(filename)
    t = TopologyExplorer(compound)
    return t.solids()


if __name__ == '__main__':
    main()
