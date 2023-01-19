from utils.common import *
from utils.vertex import VertexLabel
from utils.sort_utils import sort_graph_fragments
import networkx as nx
import networkx.algorithms.isomorphism as iso

def is_isomorphic(frag: GraphFragment) -> bool:
    G_base = nx.Graph()
    G_base.add_nodes_from(list(range(6)))
    G_base.add_edges_from([(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (2, 3), (3, 5), (4, 5), (1, 4)])

    G_frag = nx.Graph()
    vert_ids = list(map(lambda v: v.id, frag.vertices))
    G_frag.add_nodes_from(vert_ids)
    G_frag.add_edges_from(frag.edges)
    return iso.is_isomorphic(G_frag, G_base)

def P3(id):
    global vertices_graph_fragment
    global graph_fragment_list
    graph_fragment = vertices_graph_fragment.get(id) # check if a graph fragment is registered as possible to extend to lower layers

    # check number of vertices in input graph fragment 
    if len(graph_fragment.vertices) != 6: # if not 6, we shouldn't use P3
        return

    # check if graph fragment is isomorphic to base graph
    if not is_isomorphic(graph_fragment):
        return

    # check number of not connected vertexes
    middle_vertex_id = graph_fragment.middle_vertex.id

    adjacency_list = {}
    for edge_tuple in graph_fragment.edges:
        i, j = edge_tuple
        adjacency_list[i] = adjacency_list.get(i, []) + [j]
        adjacency_list[j] = adjacency_list.get(j, []) + [i]
    
    reduced_adjacency_list = { key: value for key, value in adjacency_list.items() if middle_vertex_id not in value and key != middle_vertex_id }
    
    # check number of vertices not connected to middle vertex (shouldn't happend though)
    if len(reduced_adjacency_list) != 1:
        return

    # check if all of those vertices are connected to two other vertices (shouldn't happend though)
    for key, value in reduced_adjacency_list.items():
        if len(value) != 2:
            return

    def get_vertex_from_id(id):
        return [x for x in graph_fragment.vertices if x.id == id][0]

    for key, value in reduced_adjacency_list.items(): # check if the middle vertex is in the middle of the two vertices not connected to the middle vertex
        middle = get_vertex_from_id(key)
        left = get_vertex_from_id(value[0])
        right = get_vertex_from_id(value[1])
        
        # make sure middle vertex is exactly between two other vertices
        if abs(middle.x - (left.x + right.x) / 2) > 0.0001:
            return
        if abs(middle.y - (left.y + right.y) / 2) > 0.0001:
            return  

    # check label of middle vertex
    if graph_fragment.middle_vertex.label != VertexLabel.I:
        return

    # check labels of other vertices
    for vertex in graph_fragment.vertices:
        if vertex != graph_fragment.middle_vertex and vertex.label != VertexLabel.E:
            return

    # vertex is applicable for further production
    lower_layer_squares = resolve_lower_layer_squares(graph_fragment) # get squares which a new fragment on lower level will occupy
    lower_left_vertex = find_lower_left_vertex(lower_layer_squares) # find the edge lowest vertices on the left
    lower_graph_fragment_width = math.sqrt(len(lower_layer_squares)) # length of a whole square (consisting of small squares) which the new graph fragment occupies
    middle_left_vertex_y = lower_left_vertex.y + lower_graph_fragment_width / 2
    upper_left_vertex_y = lower_left_vertex.y + lower_graph_fragment_width
    lower_middle_vertex_x = lower_left_vertex.x + lower_graph_fragment_width / 2
    lower_right_vertex_x = lower_left_vertex.x + lower_graph_fragment_width
    upper_right_square_middle_x = lower_middle_vertex_x + lower_graph_fragment_width / 4
    upper_right_square_middle_y = middle_left_vertex_y + lower_graph_fragment_width / 4
    lower_right_square_middle_y = lower_left_vertex.y + lower_graph_fragment_width / 4
    upper_left_square_middle_x = lower_left_vertex.x + lower_graph_fragment_width / 4

    lower_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, lower_left_vertex.y, lower_layer_squares) # define new graph fragment vertices coordinates
    upper_left_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_left_vertex.x, upper_left_vertex_y, lower_layer_squares)
    upper_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, upper_left_vertex_y, lower_layer_squares)
    middle_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x, middle_left_vertex_y, lower_layer_squares)
    middle_right_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_right_vertex_x, middle_left_vertex_y, lower_layer_squares)
    middle_left_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_left_vertex.x, middle_left_vertex_y, lower_layer_squares)
    upper_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x, upper_left_vertex_y, lower_layer_squares)
    lower_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(lower_middle_vertex_x, lower_left_vertex.y, lower_layer_squares)

    upper_right_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_right_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_right_square_middle_x, lower_right_square_middle_y, lower_layer_squares)
    upper_left_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_left_square_middle_x, upper_right_square_middle_y, lower_layer_squares)
    lower_left_square_middle_vertex = find_vertex_with_coordinates_and_remove_duplicates(upper_left_square_middle_x, lower_right_square_middle_y, lower_layer_squares)

    upper_left_square = upper_right_square = lower_left_square = lower_right_square = None
    for square in lower_layer_squares:
        if upper_left_square == None or square.field_id < upper_left_square.field_id:
            upper_left_square = square
    
    layer_size = 2 ** upper_left_square.layer_number
  
    # identification of squares for each new graph fragment
    for square in lower_layer_squares:
        if upper_right_square is None and square.field_id == upper_left_square.field_id + lower_graph_fragment_width / 2:
            upper_right_square = square
        if lower_left_square is None and square.field_id == upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size:
            lower_left_square = square
        if lower_right_square is None and square.field_id == (upper_left_square.field_id + (lower_graph_fragment_width / 2) * layer_size) + lower_graph_fragment_width / 2:
            lower_right_square = square
    
    upper_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_left_square)
    upper_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, upper_right_square)
    lower_left_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_left_square)
    lower_right_fragment_squares = return_graph_fragment_squares_from_upper_left_square(lower_layer_squares, lower_right_square)
    # end of identification of squares for each new graph fragment

    upper_right_fragment = GraphFragment(upper_right_fragment_squares, [upper_right_vertex,
                                                        middle_middle_vertex, middle_right_vertex,upper_middle_vertex,
                                                        upper_right_square_middle_vertex], graph_fragment.layer_number + 1, [(middle_middle_vertex.id, upper_middle_vertex.id), (upper_middle_vertex.id, upper_right_vertex.id), (upper_right_vertex.id, middle_right_vertex.id), (middle_right_vertex.id, middle_middle_vertex.id),
                           (middle_middle_vertex.id, upper_right_square_middle_vertex.id), (upper_middle_vertex.id, upper_right_square_middle_vertex.id), (upper_right_vertex.id, upper_right_square_middle_vertex.id), (middle_right_vertex.id, upper_right_square_middle_vertex.id)], upper_right_square_middle_vertex)
    lower_right_fragment = GraphFragment(lower_right_fragment_squares, [lower_right_vertex,
                                                        middle_middle_vertex, middle_right_vertex, lower_middle_vertex, lower_right_square_middle_vertex], graph_fragment.layer_number + 1, [(middle_middle_vertex.id, middle_right_vertex.id), (middle_right_vertex.id, lower_right_vertex.id), (lower_right_vertex.id, lower_middle_vertex.id), (lower_middle_vertex.id, middle_middle_vertex.id), (middle_middle_vertex.id, lower_right_square_middle_vertex.id), (middle_right_vertex.id, lower_right_square_middle_vertex.id), (lower_right_vertex.id, lower_right_square_middle_vertex.id), (lower_middle_vertex.id, lower_right_square_middle_vertex.id)], lower_right_square_middle_vertex)
    upper_left_fragment = GraphFragment(upper_left_fragment_squares, [upper_left_vertex,
                                                        middle_middle_vertex, middle_left_vertex, upper_middle_vertex,
                                                        upper_left_square_middle_vertex], graph_fragment.layer_number + 1, [(middle_middle_vertex.id, middle_left_vertex.id), (middle_left_vertex.id, upper_left_vertex.id), (upper_left_vertex.id, upper_middle_vertex.id), (upper_middle_vertex.id, middle_middle_vertex.id), (middle_middle_vertex.id, upper_left_square_middle_vertex.id), (middle_left_vertex.id, upper_left_square_middle_vertex.id), (upper_left_vertex.id, upper_left_square_middle_vertex.id), (upper_middle_vertex.id, upper_left_square_middle_vertex.id)], upper_left_square_middle_vertex)
    lower_left_fragment = GraphFragment(lower_left_fragment_squares, [lower_left_vertex,
                                                        middle_middle_vertex, middle_left_vertex,
                                                        lower_middle_vertex,lower_left_square_middle_vertex], graph_fragment.layer_number + 1,[(lower_left_vertex.id, middle_left_vertex.id), (middle_left_vertex.id, middle_middle_vertex.id),(middle_middle_vertex.id, lower_middle_vertex.id), (lower_middle_vertex.id, lower_left_vertex.id), (lower_left_vertex.id, lower_left_square_middle_vertex.id), (middle_left_vertex.id, lower_left_square_middle_vertex.id),(lower_middle_vertex.id, lower_left_square_middle_vertex.id), (middle_middle_vertex.id, lower_left_square_middle_vertex.id)], lower_left_square_middle_vertex)

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
