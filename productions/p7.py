from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments
from utils.common import merge_verticies

def P7(id1, id2, id3, id4):
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment_upper_left = vertices_graph_fragment.get(id1)
    graph_fragment_upper_right = vertices_graph_fragment.get(id2)
    graph_fragment_lower_left = vertices_graph_fragment.get(id3)
    graph_fragment_lower_right = vertices_graph_fragment.get(id4)

    graph_fragments = [graph_fragment_upper_left, graph_fragment_upper_right, graph_fragment_lower_left, graph_fragment_lower_right]

    # checks vertex id
    if None in graph_fragments:
        raise Exception("Wrong vertex id")

    # check middle vertex correctness
    if not all(map(is_middle_vertex_correct, graph_fragments)):
        raise Exception("Invalid middle vertex")

    # checks isomorphism
    if not all(map(is_graph_isomorphic, graph_fragments)):
        raise Exception("Given graph is not isomorphic to production left hand side")

    if not all(map(check_vertices_label, graph_fragments)):
        raise Exception("Invalid vertex label")


    lower_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_lower_right)
    lower_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_lower_left)

    if not compare_vertices(lower_left_vertex, lower_right_vertex):
        raise Exception("Vertices don't have the same coordinates")


    upper_right_vertex = get_upper_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    upper_left_vertex = get_upper_right_vertice_in_graph_fragment(graph_fragment_upper_left)

    if not compare_vertices(upper_right_vertex, upper_left_vertex):
        raise Exception("Vertices don't have the same coordinates")

    middle_right_vertex = get_lower_left_vertice_in_graph_fragment(graph_fragment_upper_right)
    middle_left_vertex = get_lower_right_vertice_in_graph_fragment(graph_fragment_upper_left)

    if not compare_vertices(middle_right_vertex, middle_left_vertex):
        raise Exception("Vertices don't have the same coordinates")

    # because all vertecies have the same coordinates we have to check only one
    if middle_left_vertex.x != (lower_left_vertex.x + upper_left_vertex.x)/2 and middle_left_vertex.y != (lower_left_vertex.y + upper_left_vertex.y)/2:
        raise Exception("Middle vertex in wrong position")

    merge_verticies(middle_right_vertex, middle_left_vertex, [graph_fragment_upper_right, graph_fragment_lower_right])
    merge_verticies(lower_right_vertex, lower_left_vertex, [graph_fragment_lower_right])
    merge_verticies(upper_right_vertex, upper_left_vertex, [graph_fragment_upper_right])


