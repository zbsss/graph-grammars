from utils.common import *
from utils.common import merge_verticies


def P7(id1, id2, id3, id4, vertical=False, affected_ids=[]):
    f1 = vertices_graph_fragment[id1]
    f2 = vertices_graph_fragment[id2]
    f3 = vertices_graph_fragment[id3]
    f4 = vertices_graph_fragment[id4]

    if not vertical:
        v1_right = sorted(sorted(f1.vertices, key=lambda v: -v.x)[:2], key=lambda v: v.y)
        v2_right = sorted(sorted(f2.vertices, key=lambda v: -v.x)[:2], key=lambda v: v.y)
        v3_left = sorted(sorted(f3.vertices, key=lambda v: v.x)[:2], key=lambda v: v.y)
        v4_left = sorted(sorted(f4.vertices, key=lambda v: v.x)[:2], key=lambda v: v.y)

        merge_verticies(v1_right[1], v3_left[1], [f1, f3])
        merge_verticies(v2_right[0], v4_left[0], [f2, f4])
        merge_verticies(v1_right[0], v3_left[0], [f1, f3])
        merge_verticies(v2_right[1], v3_left[0], [f2, f3])

        for id in affected_ids:
            f = vertices_graph_fragment[id]
            if v1_right[1] in f.vertices:
                merge_verticies(v1_right[1], v3_left[1], [f])
            if v2_right[0] in f.vertices:
                merge_verticies(v2_right[0], v4_left[0], [f])
            if v1_right[0] in f.vertices:
                merge_verticies(v1_right[0], v3_left[1], [f])
            if v2_right[1] in f.vertices:
                merge_verticies(v2_right[1], v3_left[0], [f])

    else:

        v1_lower = sorted(sorted(f1.vertices, key=lambda v: v.y)[:2], key=lambda v: v.x)
        v2_lower = sorted(sorted(f2.vertices, key=lambda v: v.y)[:2], key=lambda v: v.x)

        v3_upper = sorted(sorted(f3.vertices, key=lambda v: -v.y)[:2], key=lambda v: v.x)
        v4_upper = sorted(sorted(f4.vertices, key=lambda v: -v.y)[:2], key=lambda v: v.x)

        merge_verticies(v1_lower[0], v3_upper[0], [f1, f3])
        merge_verticies(v2_lower[1], v4_upper[1], [f2, f4])
        merge_verticies(v1_lower[1], v3_upper[1], [f1, f3])
        merge_verticies(v2_lower[0], v3_upper[1], [f2, f3])

        for id in affected_ids:
            f = vertices_graph_fragment[id]
            if v1_lower[0] in f.vertices:
                merge_verticies(v1_lower[0], v3_upper[0], [f])
            if v1_lower[1] in f.vertices:
                merge_verticies(v1_lower[1], v4_upper[1], [f])
            if v2_lower[1] in f.vertices:
                merge_verticies(v2_lower[1], v3_upper[1], [f])
            if v2_lower[0] in f.vertices:
                merge_verticies(v2_lower[0], v3_upper[1], [f])

    for f in [f1, f2, f3, f4]:
        f.vertices = list(set(f.vertices))
    fix_nodes_id()
