from productions.p1 import P1
from productions.p10 import P10
from productions.p11 import P11
from productions.p12 import P12
from productions.p2 import P2
from productions.p7 import P7
from utils.common import vertices_graph_fragment
from utils.graph_drawer import draw_graph

def main():

    P1(0)
    P2(5)
    P2(10)
    P2(15)
    P10(20)
    P2(25)

    P7(60, 65, 90, 95, vertical=True, affected_ids=[69])
    P11(40, 45, 69)

    P7(35, 45, 50, 60, affected_ids=[69])

    P12(69, 90, 100)
    for fragment in vertices_graph_fragment.values():
        print(f'fragment id: {fragment.middle_vertex.id}, vertices: {len(fragment.vertices)}, edges: {len(fragment.edges)}')
        print('vertices:')
        print(fragment.vertices)
        m_id = fragment.middle_vertex.id
        print('edges without connections to middle:')
        print(list(filter(lambda e: e[0] != m_id and e[1] != m_id, fragment.edges)))
    draw_graph()

if __name__ == "__main__":
    main()