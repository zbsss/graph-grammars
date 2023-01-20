from utils.common import *


def P13(i1, i2, E1, E2, E3, E4):
    global vertices_graph_fragment
    vertices_graph_fragment[i2].edges.append((min(E1, E4), max(E1, E4)))
    vertices_graph_fragment[i2].edges.append((min(E2, E3), max(E2, E3)))
    vertices_graph_fragment[i2].edges.remove((min(E3, E4), max(E3, E4)))  
    merge_vertices([E1, E3])
    merge_vertices([E2, E4])
    fix_nodes_id()