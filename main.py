from productions.p1 import P1
from productions.p3 import P3
from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():
    P1(0)
    graph_fragment = vertices_graph_fragment.get(5)
    graph_fragment.vertices.extend(list([Vertex(0, -1.5, 106, VertexLabel(1))]))
    graph_fragment.edges.extend(list([(1, 106), (3, 106)]))
    graph_fragment.edges.remove((1, 3))

    P3(5)

    draw_graph()

if __name__ == "__main__":
    main()
