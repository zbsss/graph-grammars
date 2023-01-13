import networkx as nx
import networkx.algorithms.isomorphism as iso

from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments


def P2(id):
    validate(id)
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment = vertices_graph_fragment.get(
        id)  # check if a graph fragment is registered as possible to extend to lower layers
    lower_layer_squares = resolve_lower_layer_squares(
        graph_fragment)  # get squares which a new fragment on lower level will occupy
    lower_left_vertex = find_lower_left_vertex(lower_layer_squares)  # find the edge lowest vertices on the left
    lower_graph_fragment_width = math.sqrt(
        len(lower_layer_squares))  # length of a whole square (consisting of small squares) which the new graph fragment occupies
    middle_left_vertex_y = lower_left_vertex.y + lower_graph_fragment_width / 2
    upper_left_vertex_y = lower_left_vertex.y + lower_graph_fragment_width
    lower_middle_vertex_x = lower_left_vertex.x + lower_graph_fragment_width / 2
    lower_right_vertex_x = lower_left_vertex.x + lower_graph_fragment_width
    upper_right_square_middle_x = lower_middle_vertex_x + lower_graph_fragment_width / 4
    upper_right_square_middle_y = middle_left_vertex_y + lower_graph_fragment_width / 4
    lower_right_square_middle_y = lower_left_vertex.y + lower_graph_fragment_width / 4
    upper_left_square_middle_x = lower_left_vertex.x + lower_graph_fragment_width / 4

    lower_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, lower_left_vertex.y,
                                                                            lower_layer_squares)  # define new graph fragment vertices coordinates
    upper_left_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_left_vertex.x, upper_left_vertex_y,
                                                                           lower_layer_squares)
    upper_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, upper_left_vertex_y,
                                                                            lower_layer_squares)
    middle_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x,
                                                                              middle_left_vertex_y, lower_layer_squares)
    middle_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, middle_left_vertex_y,
                                                                             lower_layer_squares)
    middle_left_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_left_vertex.x, middle_left_vertex_y,
                                                                            lower_layer_squares)
    upper_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x, upper_left_vertex_y,
                                                                             lower_layer_squares)
    lower_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x, lower_left_vertex.y,
                                                                             lower_layer_squares)

    upper_right_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_right_square_middle_x,
                                                                                          upper_right_square_middle_y,
                                                                                          lower_layer_squares)
    lower_right_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_right_square_middle_x,
                                                                                          lower_right_square_middle_y,
                                                                                          lower_layer_squares)
    upper_left_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_left_square_middle_x,
                                                                                         upper_right_square_middle_y,
                                                                                         lower_layer_squares)
    lower_left_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_left_square_middle_x,
                                                                                         lower_right_square_middle_y,
                                                                                         lower_layer_squares)

    upper_left_square = upper_right_square = lower_left_square = lower_right_square = None
    for square in lower_layer_squares:
        if upper_left_square == None or square.field_id < upper_left_square.field_id:
            upper_left_square = square

    layer_size = 2 ** upper_left_square.layer_number

    # identification of squares for each new graph fragment
    for square in lower_layer_squares:
        if upper_right_square is None and square.field_id == upper_left_square.field_id + lower_graph_fragment_width / 2:
            upper_right_square = square
        if lower_left_square is None and square.field_id == upper_left_square.field_id + (
                lower_graph_fragment_width / 2) * layer_size:
            lower_left_square = square
        if lower_right_square is None and square.field_id == (upper_left_square.field_id + (
                lower_graph_fragment_width / 2) * layer_size) + lower_graph_fragment_width / 2:
            lower_right_square = square

    upper_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares,
                                                                                       upper_left_square)
    upper_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares,
                                                                                        upper_right_square)
    lower_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares,
                                                                                       lower_left_square)
    lower_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares,
                                                                                        lower_right_square)
    # end of identification of squares for each new graph fragment

    upper_right_fragment = GraphFragment(upper_right_fragment_squares, [upper_right_vertex,
                                                                        middle_middle_vertex, middle_right_vertex,
                                                                        upper_middle_vertex,
                                                                        upper_right_square_middle_vertex],
                                         graph_fragment.layer_number + 1,
                                         [(middle_middle_vertex.id, upper_middle_vertex.id),
                                          (upper_middle_vertex.id, upper_right_vertex.id),
                                          (upper_right_vertex.id, middle_right_vertex.id),
                                          (middle_right_vertex.id, middle_middle_vertex.id),
                                          (middle_middle_vertex.id, upper_right_square_middle_vertex.id),
                                          (upper_middle_vertex.id, upper_right_square_middle_vertex.id),
                                          (upper_right_vertex.id, upper_right_square_middle_vertex.id),
                                          (middle_right_vertex.id, upper_right_square_middle_vertex.id)],
                                         upper_right_square_middle_vertex)
    lower_right_fragment = GraphFragment(lower_right_fragment_squares, [lower_right_vertex,
                                                                        middle_middle_vertex, middle_right_vertex,
                                                                        lower_middle_vertex,
                                                                        lower_right_square_middle_vertex],
                                         graph_fragment.layer_number + 1,
                                         [(middle_middle_vertex.id, middle_right_vertex.id),
                                          (middle_right_vertex.id, lower_right_vertex.id),
                                          (lower_right_vertex.id, lower_middle_vertex.id),
                                          (lower_middle_vertex.id, middle_middle_vertex.id),
                                          (middle_middle_vertex.id, lower_right_square_middle_vertex.id),
                                          (middle_right_vertex.id, lower_right_square_middle_vertex.id),
                                          (lower_right_vertex.id, lower_right_square_middle_vertex.id),
                                          (lower_middle_vertex.id, lower_right_square_middle_vertex.id)],
                                         lower_right_square_middle_vertex)
    upper_left_fragment = GraphFragment(upper_left_fragment_squares, [upper_left_vertex,
                                                                      middle_middle_vertex, middle_left_vertex,
                                                                      upper_middle_vertex,
                                                                      upper_left_square_middle_vertex],
                                        graph_fragment.layer_number + 1,
                                        [(middle_middle_vertex.id, middle_left_vertex.id),
                                         (middle_left_vertex.id, upper_left_vertex.id),
                                         (upper_left_vertex.id, upper_middle_vertex.id),
                                         (upper_middle_vertex.id, middle_middle_vertex.id),
                                         (middle_middle_vertex.id, upper_left_square_middle_vertex.id),
                                         (middle_left_vertex.id, upper_left_square_middle_vertex.id),
                                         (upper_left_vertex.id, upper_left_square_middle_vertex.id),
                                         (upper_middle_vertex.id, upper_left_square_middle_vertex.id)],
                                        upper_left_square_middle_vertex)
    lower_left_fragment = GraphFragment(lower_left_fragment_squares, [lower_left_vertex,
                                                                      middle_middle_vertex, middle_left_vertex,
                                                                      lower_middle_vertex,
                                                                      lower_left_square_middle_vertex],
                                        graph_fragment.layer_number + 1, [(lower_left_vertex.id, middle_left_vertex.id),
                                                                          (middle_left_vertex.id,
                                                                           middle_middle_vertex.id), (
                                                                          middle_middle_vertex.id,
                                                                          lower_middle_vertex.id), (
                                                                          lower_middle_vertex.id, lower_left_vertex.id),
                                                                          (lower_left_vertex.id,
                                                                           lower_left_square_middle_vertex.id), (
                                                                          middle_left_vertex.id,
                                                                          lower_left_square_middle_vertex.id), (
                                                                          lower_middle_vertex.id,
                                                                          lower_left_square_middle_vertex.id), (
                                                                          middle_middle_vertex.id,
                                                                          lower_left_square_middle_vertex.id)],
                                        lower_left_square_middle_vertex)

    vertices_graph_fragment.pop(id, None)
    set_labels_in_graph_fragment(upper_right_fragment)
    set_labels_in_graph_fragment(lower_right_fragment)
    set_labels_in_graph_fragment(upper_left_fragment)
    set_labels_in_graph_fragment(lower_left_fragment)
    vertices_graph_fragment[upper_right_fragment.middle_vertex.id] = upper_right_fragment
    vertices_graph_fragment[lower_right_fragment.middle_vertex.id] = lower_right_fragment
    vertices_graph_fragment[upper_left_fragment.middle_vertex.id] = upper_left_fragment
    vertices_graph_fragment[lower_left_fragment.middle_vertex.id] = lower_left_fragment
    graph_fragment_list.append(upper_right_fragment)
    graph_fragment_list.append(lower_right_fragment)
    graph_fragment_list.append(upper_left_fragment)
    graph_fragment_list.append(lower_left_fragment)
    inter_layer_connections.append((upper_right_fragment.middle_vertex.id, id))
    inter_layer_connections.append((lower_right_fragment.middle_vertex.id, id))
    inter_layer_connections.append((upper_left_fragment.middle_vertex.id, id))
    inter_layer_connections.append((lower_left_fragment.middle_vertex.id, id))
    graph_fragment.middle_vertex.label = VertexLabel.i
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()
    graph_fragment_list.extend(sorted_graph_fragment_list)


def validate(id):
    if vertices_graph_fragment[id] is None:
        msg = 'Fragment with id {} does not exist'.format(id)
        raise Exception(msg)
    if vertices_graph_fragment[id].middle_vertex.label.name != 'I':
        vertex_type = vertices_graph_fragment[id].middle_vertex.label.name
        msg = 'Incorrect type of middle vertex for fragment with id {}.' \
              ' Expected type is {}, but we actual type is {}'.format(id, 'I', vertex_type)
        raise Exception(msg)
    if len(vertices_graph_fragment[id].vertices) != 5:
        number_of_vertices = len(vertices_graph_fragment[id].vertices)
        msg = 'Fragment with id {} contains {} vertices, but should have 5'.format(id, number_of_vertices)
        raise Exception(msg)
    if len(vertices_graph_fragment[id].edges) != 8:
        number_of_vertices = len(vertices_graph_fragment[id].edges)
        msg = 'Fragment with id {} contains {} edges, but should have 8'.format(id, number_of_vertices)
        raise Exception(msg)
    if is_isomorphic(vertices_graph_fragment[id]) is False:
        msg = 'Fragment with id {} is not isomorphic to left side of production'.format(id)
        raise Exception(msg)


def is_isomorphic(frag: GraphFragment) -> bool:
    graph_fragment = nx.Graph()
    vert_ids = list(map(lambda v: v.id, frag.vertices))
    graph_fragment.add_nodes_from(vert_ids)
    graph_fragment.add_edges_from(frag.edges)
    g_base = create_base_graph()
    return iso.is_isomorphic(graph_fragment, g_base)


def create_base_graph():
    g = nx.Graph()
    g.add_nodes_from(list(range(5)))
    g.add_edges_from([(0, 1), (0, 2), (0, 4), (1, 4), (1, 3), (2, 3), (2, 4), (3, 4)])
    return g
