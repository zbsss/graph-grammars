from productions.p1 import P1
from productions.p10 import P10
from productions.p11 import P11
from productions.p12 import P12
from productions.p2 import P2
from productions.p7 import P7
from productions.p9 import P9
from productions.p3 import P3
from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():
    global vertices_graph_fragment

    P1(0)

    P2(5)

    P2(10)
    P2(15)
    P10(20)
    P2(25)

    P7(60, 65, 90, 95, vertical=True, affected_ids=[69])
    P11(40, 45, 69)

    P7(35, 45, 50, 60, affected_ids=[69])
    # print(vertices_graph_frament)

    P12(69, 90, 100)
    for fragment in vertices_graph_fragment.values():
        print(fragment.middle_vertex.id, len(fragment.vertices), len(fragment.edges))
    # print(vertices_graph_fragment)
    draw_graph()

    # draw_graph()

if __name__ == "__main__":
    main()
# x: 2, y: -8