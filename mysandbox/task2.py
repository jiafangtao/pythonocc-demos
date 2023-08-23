#! /usr/bin/env python3

#
# Task 2: dump a stp file
#

from OCC.Extend.DataExchange import read_step_file
from OCC.Extend.TopologyUtils import (
    TopologyExplorer,
    get_type_as_string,
    dump_topology_to_string
)

def main(file_path):
    shp = read_step_file(file_path)
    topo = TopologyExplorer(shp)
    for solid in topo.solids():
        print(get_type_as_string(solid))

    dump_topology_to_string(shp)

if __name__ == '__main__':
    main("dianzijixiang.stp")
