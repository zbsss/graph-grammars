from productions.p1 import P1
from productions.p2 import P2
from productions.p7 import P7
from utils.common import *
from utils.vertex import VertexLabel
import unittest


class TestP7(unittest.TestCase):
    def setUp(self):
        prepare_graph()

    def tearDown(self):
        reset_global_state()

    def test_succeess(self):
        P7(35, 50, 45, 60)
        graph_fragment_upper_left = vertices_graph_fragment.get(35)
        graph_fragment_upper_right = vertices_graph_fragment.get(50)
        graph_fragment_lower_left = vertices_graph_fragment.get(45)
        graph_fragment_lower_right = vertices_graph_fragment.get(60)
        lower_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)
        lower_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)
        self.assertEqual(lower_left_vertex.id, lower_right_vertex.id)
        upper_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        upper_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        self.assertEqual(upper_right_vertex.id, upper_left_vertex.id)
        middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
        middle_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)
        self.assertEqual(middle_right_vertex.id, middle_left_vertex.id)


    def test_fail_on_invalid_middle_label(self):
        graph = vertices_graph_fragment.get(50)
        graph.middle_vertex.label = VertexLabel.i
        self.assertRaises(Exception, lambda: P7(35, 50, 45, 60))

    def test_fail_on_invalid_edge_label(self):
        graph = vertices_graph_fragment.get(50)
        graph.vertices[0].label = VertexLabel.i
        self.assertRaises(Exception, lambda: P7(35, 50, 45, 60))

    def test_fail_on_invalid_middle_coords(self):
        graph = vertices_graph_fragment.get(50)
        graph.middle_vertex.x = -3
        graph.middle_vertex.y = -3
        self.assertRaises(Exception, lambda: P7(35, 50, 45, 60))

    def test_fail_on_invalid_edge_coords(self):
        graph = vertices_graph_fragment.get(50)
        graph.vertices[0].x = 0.8
        self.assertRaises(Exception, lambda: P7(35, 50, 45, 60))

    def test_fail_on_invalid_edges(self):
        graph = vertices_graph_fragment.get(50)
        graph.edges.remove((46, 47))
        self.assertRaises(Exception, lambda: P7(35, 50, 45, 60))


def prepare_graph():
    P1(0)
    P2(5)
    P2(10)
    P2(15)
