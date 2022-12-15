from utils.graph_drawer import draw_graph
from productions.p1 import P1
from productions.p2 import P2
from productions.p9 import P9


def main():
    P1(0)
    P2(5)

    ####### p9 test
    P2(15)
    P2(25)
    #P9(35,45,50,60)    ### TEST HORIZONTAL
    P9(50,55,40,45)     ### TEST VERTICAL
    #######

    draw_graph()

if __name__ == "__main__":
    main()
