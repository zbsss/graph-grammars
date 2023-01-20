from productions.p1 import P1
from productions.p10 import P10
from productions.p2 import P2
from productions.p7 import P7
from productions.p9 import P9
from productions.p3 import P3
from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():

    P1(0)

    P2(5)

    P2(10)
    P2(15)
    P10(20)
    P2(25)

    P7(60, 65, 90, 95)
    P7(35, 50, 45, 60)

    draw_graph()

if __name__ == "__main__":
    main()
