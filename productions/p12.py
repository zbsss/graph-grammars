from utils.common import *


def P12(id1, id2, id3):
    global vertices_graph_fragment

    f1 = vertices_graph_fragment[id1]
    f2 = vertices_graph_fragment[id2]
    f3 = vertices_graph_fragment[id3]

    right_most = sorted(sorted(f1.vertices, key=lambda v: -v.x)[:2], key=lambda v: v.y)
    left_most = sorted(sorted(f2.vertices + f3.vertices, key=lambda v: v.x)[:3], key=lambda v: v.y)

    print(f1.edges)
    print(right_most)
    try:
        f1.edges.remove((right_most[0].id, right_most[1].id))
    except:
        f1.edges.remove((right_most[1].id, right_most[0].id))

    if left_most[0] in f2.vertices:
        merge_verticies(right_most[0], left_most[0], [f1, f2])
    else:
        merge_verticies(right_most[0], left_most[0], [f1, f3])

    f1.vertices.append(left_most[1])
    f1.edges.append((left_most[1].id, left_most[0].id))
    f1.edges.append((left_most[2].id, left_most[1].id))
    print(f1.edges)


    print(f1.edges)
    fix_nodes_id()
