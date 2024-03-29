import productions.p3, productions.p1, utils.common
from utils.vertex import Vertex, VertexLabel
import unittest, importlib

def reload_libs():
    importlib.reload(utils.common)
    importlib.reload(productions.p1)
    importlib.reload(productions.p3)

class P3TestMethods(unittest.TestCase):
    # correct circumstances - 1 broken edge with vertex in between
    def test_one_broken_edge(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment

        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106)]))
        graph_fragment.edges.remove((1, 3))
        P3(5)
        self.assertIsNotNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - 2 broken edges with vertex in between of them
    def test_too_many_broken_edges(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment

        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1)),  Vertex(0.5, -1, 107, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106), (2, 107), (1, 107)]))
        graph_fragment.edges.remove((1, 3))
        graph_fragment.edges.remove((1, 2))
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - not a single broken edge
    def test_no_broken_edges(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment
        
        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - 1 broken edge with vertex in between but it's also connected to middle vertex
    def test_broken_edge_vertice_connected_to_middle_vertex(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment
        
        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106), (5, 106)]))
        graph_fragment.edges.remove((1, 3))
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - 1 broken edge with vertex in between but it's not connected to any other vertex
    def test_broken_edge_vertice_not_connected(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment
        
        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - 1 broken edge with vertex in between but it's in the wrong position (not in the middle of them)
    def test_wrong_position_of_broken_edge(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment
        
        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.4, 106, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106)]))
        graph_fragment.edges.remove((1, 3))
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - incorrect label of at least 1 vertices (excluding middle vertex)
    def test_wrong_label_vertice(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment

        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106)]))
        graph_fragment.edges.remove((1, 3))
        graph_fragment.vertices[1].label = VertexLabel.I # have wrong label for at least one vertex (excluding middle one)
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

    # incorrect circumstances - incorrect label of middle vertex (it's not I)
    def test_wrong_label_middle_vertice(self):
        reload_libs()
        P1 = productions.p1.P1
        P3 = productions.p3.P3
        vertices_graph_fragment = utils.common.vertices_graph_fragment

        P1(0)
        graph_fragment = vertices_graph_fragment.get(5)
        graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
        graph_fragment.edges.extend(list([(1, 106), (3, 106)]))
        graph_fragment.edges.remove((1, 3))
        graph_fragment.middle_vertex.label = VertexLabel.i # have wrong label for middle vertex
        P3(5)
        self.assertIsNone(vertices_graph_fragment.get(10))

if __name__ == '__main__':
    unittest.main() 