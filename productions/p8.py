from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments
from utils.common import merge_verticies


def P8(id1, id2, id3, id4):
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment_upper_left = vertices_graph_fragment.get(id1)
    graph_fragment_upper_right = vertices_graph_fragment.get(id2)
    graph_fragment_lower_left = vertices_graph_fragment.get(id3)
    graph_fragment_lower_right = vertices_graph_fragment.get(id4)
    # print(graph_fragment_upper_left)
    # print(graph_fragment_upper_right)
    # print(graph_fragment_lower_left)
    # print(graph_fragment_lower_right)
    # print(graph_fragment_upper_left.vertices)
    # for v in graph_fragment_upper_left.vertices:
    #     print(v.x, v.y, v.id)

    #top_left_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_left)
    #bottom_left_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_lower_left)
    
    middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    middle_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)

    print("middle_right_vertex",middle_right_vertex.id)
    print("middle_left_vertex",middle_left_vertex.id)


    lower_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)
    lower_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)


    # upper_middle_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)

    # lower_middle_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    # bottom_right_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_lower_right)

    merge_verticies(middle_right_vertex, middle_left_vertex, [graph_fragment_upper_right, graph_fragment_lower_right])
    merge_verticies(lower_right_vertex, lower_left_vertex, [graph_fragment_lower_right])

