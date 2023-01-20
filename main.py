from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9
from productions.p3 import P3
from productions.p11_p12_p13 import P11, P12, P13
from utils.graph_drawer import draw_graph, set_position_move
from utils.vertex import Vertex, VertexLabel
from utils.common import vertices_graph_fragment, set_split_nodes

def P10(v):
    P1(v)
    
def TaskE():
    set_position_move(False)

    P1(0)
    draw_graph()
    P2(5)
    draw_graph()

    P2(15)
    P10(10)
    P10(20)
    P10(25)
    #draw_graph()

    P13(69, 89, 72, 84, 86, 98)
    #draw_graph()

    P13(49, 69, 58, 64, 66, 72)
    #draw_graph()
 
    P11(45, 40, 89, 44, 39, 38, 92, 64)
    #draw_graph()

    P12(40, 30, 49, 38, 28, 26, 52)
    draw_graph()
    

    P2(35)
    P10(49)
    P10(69)
    P10(89)
    P10(30)
    P10(40)
    P10(45)
    #draw_graph()

    P13(389, 409, 392, 404, 406, 418)
    #draw_graph()

    P13(369, 389, 378, 384, 386, 392)
    #draw_graph()

    P11(120, 110, 369, 118, 108, 106, 384, 372)
    #draw_graph()

    P12(120, 125, 409, 118, 119, 124, 412)
    #draw_graph()
    
    P13(144, 224, 178, 204, 206, 232)
    P13(224, 304, 204, 284, 286, 338)
    #draw_graph()

    P11(389, 369, 144, 398, 378, 366, 204, 152)
    #draw_graph()

    P12(389, 409, 304, 204, 404, 424, 312)
    draw_graph()

    P2(115)
    P10(144)
    P10(224)
    P10(304)
    P10(369)
    P10(389)
    P10(409)
    P10(110)
    P10(120)
    P10(125)
    #draw_graph()

    P13(1669, 1689, 1672, 1684, 1686, 1698)
    P13(1649, 1669, 1658, 1664, 1666, 1672)
    #draw_graph()

    P11(440, 445, 1689, 438, 439, 444, 1664, 1692)
    P12(440, 430, 1649, 438, 428, 426, 1652)
    #draw_graph()

    P13(1504, 1584, 1512, 1564, 1566, 1618)
    P13(1424, 1504, 1458, 1484, 1486, 1512)

    P11(1669, 1689, 1584, 1678, 1684, 1704, 1484, 1592)
    P12(1669, 1649, 1424, 1484, 1658, 1646, 1432)

    P13(844, 1164, 872, 1084, 1086, 1298)
    P13(524, 844, 658, 764, 766, 872)

    P11(1504, 1584, 1164, 1538, 1564, 1644, 764, 1192)
    P12(1504, 1424, 524, 764, 1458, 1406, 552)
    draw_graph()

def main():
    TaskE()
   

if __name__ == "__main__":
    main()
