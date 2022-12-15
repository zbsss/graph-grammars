from productions.p1 import P1
from productions.p6 import P6, is_isomorphic
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph
from utils.graph_fragment import GraphFragment
from utils.vertex import Vertex, VertexLabel


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
    edges = [(0, 10), (0, 30), (0, 50), (0, 70), (10, 20), (20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80), (80, 10)]
    return GraphFragment(squares=[], vertices=vertices, edges=edges, layer_number=0, middle_vertex=mid_vertex)
def test_isomorphism():
    print(is_isomorphic(get_isomorphic_graph_fragment()))

def test_success():
    P1(0)
    graph_fragment = vertices_graph_fragment.get(5)
    print(list(map(lambda v: (v.x, v.y, v.id), graph_fragment.vertices)))
    graph_fragment.vertices.extend(list([Vertex(0, -1.5, 100, VertexLabel.E), Vertex(0.5, -1, 200, VertexLabel.E), Vertex(1, -1.5, 300, VertexLabel.E), Vertex(0.5, -2, 400, VertexLabel.E)]))
    graph_fragment.edges.extend(list([(3, 100), (100, 1), (1, 200), (200, 2), (2, 300), (300, 4), (4, 400), (400, 3)]))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((1, 2))
    graph_fragment.edges.remove((4, 2))
    graph_fragment.edges.remove((3, 4))
    print(graph_fragment.edges)
    print(list(map(lambda v: v.label, graph_fragment.vertices)))
    P6(5)
    draw_graph()

test_isomorphism()
test_success()