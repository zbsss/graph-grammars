import unittest

from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9
from utils.graph_drawer import draw_graph
from utils.common import *

def reset_all():
    global _BETWEEN_LAYER_BUFFER 
    global _graph_vertices_id_counter
    global _start_vertex
    global _start_fragment
    global vertices_graph_fragment
    global graph_fragment_list
    global inter_layer_connections

    _BETWEEN_LAYER_BUFFER = 1  # possible to modify
    _graph_vertices_id_counter = 1
    _start_vertex = Vertex(0, 0, 0, VertexLabel.I)
    _start_fragment = GraphFragment([], [_start_vertex], -1, [], _start_vertex)
    vertices_graph_fragment = {0: _start_fragment}
    graph_fragment_list = [_start_fragment]
    inter_layer_connections = []

class TestP2(unittest.TestCase):

    def setUp(self):
        pass


    def test_vertical(self):
        P1(0)
        P2(5)
        P2(15)
        P2(25)
        merge_vertices([38,46])   
        merge_vertices([44,52])   
        P9(50,55,40,45)   

        draw_graph()

    def test_horizontal(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)

        merge_vertices([32, 46])    
        merge_vertices([44,58])    
        P9(35,45,50,60)

        draw_graph()