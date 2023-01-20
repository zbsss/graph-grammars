from utils.common import *


def P14(E1, E2):
    global vertices_graph_fragment
    merge_vertices([E1, E2])
    fix_nodes_id()