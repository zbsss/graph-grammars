from utils.graph_drawer import draw_graph
from productions.p1 import P1
from productions.p2 import P2
from productions.p8 import P8
from productions.p7 import P7
from utils.common import *

def main():
    P1(0)
    P2(5)
    P2(10)
    P2(15)
    graph_fragment_upper_left = vertices_graph_fragment.get(35)
    graph_fragment_upper_right = vertices_graph_fragment.get(50)
    upper_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    upper_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)
    merge_verticies(upper_right_vertex, upper_left_vertex, [graph_fragment_upper_right])


    draw_graph()

if __name__ == "__main__":
    main()
