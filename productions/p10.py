from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments


def P10(id): #P1 with changed label
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment = vertices_graph_fragment.get(id)  # check if a graph fragment is registered as possible to extend to lower layers
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment)  # get squares which a new fragment on lower level will occupy
    lower_left_vertex = find_lower_left_vertex(lower_layer_squares)  # find the edge lowest vertex on the left
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares))  # length of a whole square (consisting of small squares) which the new graph fragment occupies
    lower_right_x = lower_left_vertex.x + lower_graph_fragment_width  # define new graph fragment vertices coordinates
    lower_right_y = lower_left_vertex.y
    upper_left_x = lower_left_vertex.x
    upper_left_y = lower_left_vertex.y + lower_graph_fragment_width
    upper_right_x = lower_right_x
    upper_right_y = upper_left_y
    middle_x = lower_left_vertex.x + (lower_graph_fragment_width / 2)
    middle_y = lower_left_vertex.y + (lower_graph_fragment_width / 2)
    lower_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_x, lower_right_y, # define vertices and remove duplicate vertices for neighboring squares
                                                                              lower_layer_squares)
    upper_left_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_left_x, upper_left_y,
                                                                             lower_layer_squares)
    upper_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_right_x, upper_right_y,
                                                                              lower_layer_squares)
    middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(middle_x, middle_y, lower_layer_squares)

    edges = [(upper_left_vertex.id, lower_left_vertex.id), (upper_left_vertex.id, upper_right_vertex.id),   # define edges (connections between vertices (their ids))
             (upper_left_vertex.id, middle_vertex.id),
             (lower_left_vertex.id, lower_right_vertex.id), (lower_left_vertex.id, middle_vertex.id),
             (lower_right_vertex.id, middle_vertex.id),
             (lower_right_vertex.id, upper_right_vertex.id), (upper_right_vertex.id, middle_vertex.id)]
    new_fragment = GraphFragment(lower_layer_squares,   # define new graph fragment on lower layer
                                [lower_left_vertex, lower_right_vertex, upper_left_vertex, upper_right_vertex,
                                middle_vertex], graph_fragment.layer_number + 1, edges,
                                middle_vertex)
    vertices_graph_fragment.pop(id, None)  # remove old fragment (the one from which we were generating the lower one) from the list of registered graph fragments to generate something from it
    vertices_graph_fragment[middle_vertex.id] = new_fragment  # register the new lower fragment as a one from which you can generate something
    graph_fragment_list.append(new_fragment)  # add fragment to a graph list
    inter_layer_connections.append((middle_vertex.id, id))  # create connection between graph fragments (also between layers)
    set_labels_in_graph_fragment(new_fragment)
    new_fragment.middle_vertex.label = VertexLabel.i
    graph_fragment.middle_vertex.label = VertexLabel.i  # set upper graph fragment middle vertex label to i - occupied
    sorted_graph_fragment_list = sort_graph_fragments(graph_fragment_list)
    graph_fragment_list.clear()
    graph_fragment_list.extend(sorted_graph_fragment_list)  # update graph_fragment_list to sorted one

