from productions.p1 import P1
from productions.p4 import P4
from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

# WIP
def first_test():
    P1(0)

    graph_fragment = vertices_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1)),  Vertex(0.5, -1, 107, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 106), (3, 106), (2, 107), (1, 107)]))
    graph_fragment.edges.remove((1, 3))
    graph_fragment.edges.remove((1, 2))

    P4(5)

    draw_graph()