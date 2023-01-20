from utils.common import *


def P12(i1, i2, i3, E1, E2, E3, E4):
    global vertices_graph_fragment
    vertices_graph_fragment[i3].edges.append((min(E2, E4), max(E2, E4)))
    vertices_graph_fragment[i3].edges.remove((min(E1, E4), max(E1, E4)))  

    merge_vertices([E3, E4])
    fix_nodes_id()
