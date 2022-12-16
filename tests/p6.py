from productions.p1 import P1
from productions.p6 import P6, is_isomorphic
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph, graph_fragment_list
from utils.graph_fragment import GraphFragment
from utils.vertex import Vertex, VertexLabel
import unittest


class TestP5(unittest.TestCase):

    def test_isomorphism(self):
        self.assertTrue(is_isomorphic(get_isomorphic_graph_fragment()))

    def test_succeess(self):
        prepare_graph()
        P6(5)
        draw_graph()
        self.assertEquals(len(graph_fragment_list), 6)

    def test_fail_on_invalid_middle_label(self):
        graph_fragment = prepare_graph()
        graph_fragment.middle_vertex.label = VertexLabel.i
        draw_graph()
        self.assertRaises(Exception, lambda: P6(5))

    def test_fail_on_invalid_edge_label(self):
        graph_fragment = prepare_graph()
        graph_fragment.vertices[5].label = VertexLabel.I
        draw_graph()
        self.assertRaises(Exception, lambda: P6(5))

    def test_fail_on_invalid_middle_coords(self):
        graph_fragment = prepare_graph()
        graph_fragment.middle_vertex.x = -3
        graph_fragment.middle_vertex.y = -3
        draw_graph()
        self.assertRaises(Exception, lambda: P6(5))

    def test_fail_on_invalid_edge_coords(self):
        graph_fragment = prepare_graph()
        graph_fragment.vertices[6].x = 0.8
        draw_graph()
        self.assertRaises(Exception, lambda: P6(5))

    def test_fail_on_invalid_edges(self):
        graph_fragment = prepare_graph()
        graph_fragment.edges.remove((1, 200))
        draw_graph()
        self.assertRaises(Exception, lambda: P6(5))


def prepare_graph() -> GraphFragment:
    P1(0)
    graph_fragment = vertices_graph_fragment[5]
    graph_fragment.vertices.extend(list([Vertex(0, -1.5, 100, VertexLabel.E), Vertex(0.5, -1, 200, VertexLabel.E),
                                         Vertex(1, -1.5, 300, VertexLabel.E), Vertex(0.5, -2, 400, VertexLabel.E)]))
    graph_fragment.edges.extend(
        list([(3, 100), (100, 1), (1, 200), (200, 2), (2, 300), (300, 4), (4, 400), (400, 3)]))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    return graph_fragment


def get_isomorphic_graph_fragment() -> GraphFragment:
    mid_vertex = Vertex(1, 1, 0, VertexLabel.I)
    vertices = [mid_vertex,
                Vertex(0, 0, 10, VertexLabel.E),
                Vertex(0, 1, 20, VertexLabel.E),
                Vertex(0, 2, 30, VertexLabel.E),
                Vertex(1, 2, 40, VertexLabel.E),
                Vertex(2, 2, 50, VertexLabel.E),
                Vertex(2, 1, 60, VertexLabel.E),
                Vertex(2, 0, 70, VertexLabel.E),
                Vertex(1, 0, 80, VertexLabel.E)]
    edges = [(0, 10), (0, 30), (0, 50), (0, 70), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80),
             (80, 10)]
    return GraphFragment(squares=[], vertices=vertices, edges=edges, layer_number=0, middle_vertex=mid_vertex)
