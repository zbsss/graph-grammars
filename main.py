from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9
from productions.p3 import P3
from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():

    P1(0)
    P2(5)
    P2(20)
    P1(25)
    draw_graph()

if __name__ == "__main__":
    main()
