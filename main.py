from utils.graph_drawer import draw_graph
from productions.p1 import P1
from productions.p2 import P2

def main():
    P1(0)
    P2(5)

    draw_graph()

if __name__ == "__main__":
    main()
