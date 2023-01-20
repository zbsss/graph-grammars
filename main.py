from productions.p1 import P1
from productions.p2 import P2
from productions.p3 import P3
from productions.p4 import P4
from productions.p5 import P5
from productions.p6 import P6
from productions.p7 import P7
from productions.p8 import P8
from productions.p9 import P9

from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():

    P1(0)
    P2(5)

    P2(15)


    P2(25)


    P7(40, 45, 50, 55)
    
    P2(35)
    P2(45)

    P7(80, 85, 90, 95)

    P2(55)
    P2(65)

    P7(100, 105, 110, 115)
    P7(120, 125, 130, 135)

    draw_graph()

if __name__ == "__main__":
    main()
