from utils.common import *


def P11(i1, i2, i3, E1, E2, E3, E4, E5):
    global vertices_graph_fragment
    vertices_graph_fragment[i3].edges.append((min(E2, E4), max(E2, E4)))
    vertices_graph_fragment[i3].edges.append((min(E2, E5), max(E2, E5)))
    vertices_graph_fragment[i3].edges.remove((min(E4, E5), max(E4, E5)))  

    merge_vertices([E1, E4])
    merge_vertices([E3, E5])
    fix_nodes_id()