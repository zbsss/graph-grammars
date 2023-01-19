from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9
from productions.p3 import P3
from productions.p11 import P11, P12, P13
from utils.graph_drawer import draw_graph, set_position_move
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment, set_split_nodes

def P10(v):
    P1(v)

def main():

    set_position_move(True)

    P1(0)
    P2(5)
    draw_graph()

    P2(15)
    P10(10)
    P10(20)
    P10(25)
    draw_graph()

    P13(69, 89, 72, 84, 86, 98)
    draw_graph()

    P13(49, 69, 58, 64, 66, 72)
    draw_graph()
 
    P11(45, 40, 89, 44, 39, 38, 92, 64)
    draw_graph()

    P12(40, 30, 49, 38, 28, 26, 52)
    draw_graph()
    

    P2(35)
    P10(49)
    P10(69)
    P10(89)
    P10(30)
    P10(40)
    P10(45)
    draw_graph()

 # Źle IDki, ale sposób dobry
    # P13(252, 332, 229, 279, 288, 338)
    # draw_graph()
    
    # P13(172, 252, 178, 199, 208, 229)
    # draw_graph()
    
    # P13(389, 409, 392, 404, 406, 418)
    # draw_graph()

    # P13(369, 389, 378, 384, 386, 392)
    # draw_graph()

    # P11(125, 120, 409, 124, 119, 118, 412, 384)
    # draw_graph()

    # P12(120, 110, 369, 118, 108, 106, 372)
    # draw_graph()

    # P11(409, 389, 332, 424, 404, 398, 309, 199)
    # draw_graph()

    # P12(389, 369, 172, 199, 378, 366, 149)

    # draw_graph()

if __name__ == "__main__":
    main()
