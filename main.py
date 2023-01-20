from productions.p1 import P1
from productions.p2 import P2
from productions.p3 import P3
from productions.p4 import P4
from productions.p5 import P5
from productions.p6 import P6
from productions.p7 import P7
from productions.p8 import P8
from productions.p9 import P9
from productions.p10 import P10
from productions.p11 import P11
from productions.p13 import P13
from productions.p14 import P14

from utils.graph_drawer import draw_graph
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment

def main():
    # warstwa zero
    P1(0)

    # pierwsza warstwa
    P2(5)

    # druga warstwa
    P2(15)
    P2(25)

    P10(10)
    P10(20)

    # druga warstwa łączenie
    P7(40, 45, 50, 55)

    
    P11(40, 30, 69, 46, 28, 26, 84, 72)
    P13(69, 89, 78, 46, 86, 92)
    P14(104, 58)

    # trzecia warstwa
    P10(69)
    P10(89)

    P10(30)
    P10(40)
    P10(50)
    P10(60)

    P2(35)
    P2(45)
    P2(55)
    P2(65)

    # trzecia warstwa łaczenie
    P13(124, 204, 158, 184, 186, 212)
    # TODO


    draw_graph()

if __name__ == "__main__":
    main()
