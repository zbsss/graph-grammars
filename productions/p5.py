from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments
import networkx as nx
import networkx.algorithms.isomorphism as iso

G_base = nx.Graph()
G_base.add_nodes_from(list(range(8)))
G_base.add_edges_from([(0, 1), (0, 3), (0, 5), (0, 7), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)])


def is_isomorphic(frag: GraphFragment) -> bool:
    G_frag = nx.Graph()
    vert_ids = list(map(lambda v: v.id, frag.vertices))
    G_frag.add_nodes_from(vert_ids)
    G_frag.add_edges_from(frag.edges)
    return iso.is_isomorphic(G_frag, G_base)


def are_label_numbers_valid(frag: GraphFragment) -> bool:
    labels = list(map(lambda v: v.label, frag.vertices))
    return VertexLabel.I in labels and len(list(filter(lambda l: l == VertexLabel.E, labels))) == 7


def is_valid_thruple(thruple: list) -> bool:
    i = 0
    diff_y = thruple[1].y - thruple[0].y
    while i < 3:
        if thruple[i].x != thruple[0].x or thruple[i].y - thruple[0].y != i * diff_y:
            break
        i += 1
    if i == 3:
        return True
    i = 0
    diff_x = thruple[1].x - thruple[0].x
    while i < 3:
        if thruple[i].y != thruple[0].y or thruple[i].x - thruple[0].x != i * diff_x:
            break
        i += 1
    if i == 3:
        return True
    return False


def is_middle_correct(frag: GraphFragment, v_by_x: list, v_by_y: list) -> bool:
    x = v_by_x[0].x + (v_by_x[-1].x - v_by_x[0].x) / 2
    y = v_by_y[0].y + (v_by_y[-1].y - v_by_y[0].y) / 2
    return frag.middle_vertex.label == VertexLabel.I and frag.middle_vertex.x == x and frag.middle_vertex.y == y


def validate(frag: GraphFragment) -> None:
    # check if graph is isomorphic with left side of P5 and if labels are correct
    if not is_isomorphic(frag):
        raise Exception("Graph is not isomorphic with the left side of P5")
    if not are_label_numbers_valid(frag):
        raise Exception("Labels are not valid")

    # check coordinates of vertices
    v_by_x = sorted(frag.vertices, key=lambda v: v.x)
    v_by_y = sorted(frag.vertices, key=lambda v: v.y)

    # check the middle vertex
    if not is_middle_correct(frag, v_by_x, v_by_y):
        raise Exception("Invalid I vertex placement")

    # check if there are three "divided edges"
    left = sorted(v_by_x[:3], key=lambda v: v.y)
    right = sorted(v_by_x[-3:], key=lambda v: v.y)

    upper = sorted(v_by_y[-3:], key=lambda v: v.x)
    lower = sorted(v_by_y[:3], key=lambda v: v.x)

    thruples_valid = list(map(lambda thruple: is_valid_thruple(thruple), [left, right, upper, lower]))
    thruples_valid = list(filter(lambda is_valid: is_valid, thruples_valid))

    if len(thruples_valid) != 3:
        raise Exception("Invalid E vertex placement")


def P5(id: int):
    global vertices_graph_fragment
    global graph_fragment_list

    graph_fragment: GraphFragment = vertices_graph_fragment[id]

    validate(graph_fragment)

    lower_layer_squares: list[Square] = resolve_lower_layer_squares(
        graph_fragment)  # get squares which a new fragment on lower level will occupy

    lower_left_vertex: Vertex = find_lower_left_vertex(lower_layer_squares)  # find the edge lowest vertices on the left
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

    upper_right_square = lower_left_square = lower_right_square = None

    upper_left_square = sorted(lower_layer_squares, key=lambda square: square.field_id)[0]

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

    upper_right_fragment = GraphFragment(upper_right_fragment_squares,
                                         [upper_right_vertex, middle_middle_vertex,
                                          middle_right_vertex, upper_middle_vertex,
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
    lower_left_fragment = GraphFragment(lower_left_fragment_squares,
                                        [
                                            lower_left_vertex,
                                            middle_middle_vertex,
                                            middle_left_vertex,
                                            lower_middle_vertex,
                                            lower_left_square_middle_vertex
                                        ],
                                        graph_fragment.layer_number + 1,
                                        [(lower_left_vertex.id, middle_left_vertex.id),
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
    fix_nodes_id()
