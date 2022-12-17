from utils.graph_drawer import draw_graph
from productions.p1 import P1
from productions.p2 import P2
from productions.p8 import P8
from productions.p7 import P7

def main():
    P1(0)
    P2(5)
    P2(10)
    P2(15)
    P2(25)
    P2(20)

    P7(95, 70, 105, 80)
    # P8(95, 70, 105, 80)
    P8(35, 50, 45, 60)

    draw_graph()

if __name__ == "__main__":
    main()
