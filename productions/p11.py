from utils.common import *


def P11(id1, id2, id3):
    global vertices_graph_fragment

    graph_fragment_1 = vertices_graph_fragment[id1]
    graph_fragment_2 = vertices_graph_fragment[id2]
    graph_fragment_3 = vertices_graph_fragment[id3]

    print(graph_fragment_3.vertices)
    print(graph_fragment_3.edges)

    lower_1 = sorted(sorted(graph_fragment_1.vertices, key=lambda v: v.y)[:2], key=lambda v: v.x)
    lower_left = lower_1[0]
    print(lower_left)
    lower_2 = sorted(sorted(graph_fragment_2.vertices, key=lambda v: v.y)[:2], key=lambda v: -v.x)
    lower_right = lower_2[0]
    upper_left = sorted(sorted(graph_fragment_3.vertices, key=lambda v: -v.y), key=lambda v: v.x)[0]
    upper_right = sorted(sorted(graph_fragment_3.vertices, key=lambda v: -v.y), key=lambda v: -v.x)[0]
    merge_verticies(upper_left, lower_left,  [graph_fragment_1, graph_fragment_3])
    merge_verticies(upper_right, lower_right, [graph_fragment_2, graph_fragment_3])
    middle = lower_1[1]
    graph_fragment_3.vertices.append(middle)
    graph_fragment_3.edges += [(lower_left.id, middle.id), (middle.id, lower_right.id)]
    fix_nodes_id()
    try:
        graph_fragment_3.edges.remove((lower_left.id, lower_right.id))
    except:
        graph_fragment_3.edges.remove((lower_right.id, lower_left.id))
