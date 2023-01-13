import unittest

from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9
from utils.graph_drawer import draw_graph
from utils.common import *


class TestP9(unittest.TestCase):

    def setUp(self):
        pass
    def tearDown(self):
        reset_global_state()

    def test_vertical(self):
        P1(0)
        P2(5)
        P2(15)
        P2(25)
        P2(10)
        P2(20)
        merge_vertices([38,46])   
        merge_vertices([44,52])   
        P9(50,55,40,45)   

    def test_horizontal(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        P9(35,45,50,60)

    def test_horizontal_no_merge1(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        #merge_vertices([44,58]) 
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_no_edge_leafs(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        global vertices_graph_fragment
        vertices_graph_fragment[35].edges.remove((32, 34))
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_no_edge_center(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        global vertices_graph_fragment
        vertices_graph_fragment[35].edges.remove((34, 35))
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_no_edge_upper(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        global inter_layer_connections
        inter_layer_connections.remove((35, 20))
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_wrong_label_center(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        find_vertex_with_id(35).label = VertexLabel.E
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_wrong_label_leaf(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        find_vertex_with_id(32).label = VertexLabel.i
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_wrong_label_upper(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        find_vertex_with_id(20).label = VertexLabel.E
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))

    def test_horizontal_wrong_position(self):
        P1(0)
        P2(5)
        P2(20)
        P2(25)
        merge_vertices([32, 46])    
        merge_vertices([44,58]) 
        find_vertex_with_id(34).x = 0
        draw_graph()
        self.assertRaises(ValueError, lambda: P9(35,45,50,60))