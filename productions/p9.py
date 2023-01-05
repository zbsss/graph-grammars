from utils.common import *

def find_shared_connected_node(i1, i2, generator):
    """
    finds node which connects to both input nodes using provided generator from common.py
    """
    shared_nodes = []
    for edge in generator():
        if(edge[0] == i1):
            other = edge[1]
        elif(edge[1] == i1):
            other = edge[0]
        else:
            continue
        
        for edge in generator():
            if(edge[0] == i2 and edge[1] == other):
                shared_nodes.append(other)
            elif(edge[1] == i2 and edge[0] == other):
                shared_nodes.append(other)
    return shared_nodes

def edge_exists(i1, i2, generator):
    """
    returns true if edge between 2 nodes exist using provided generator from common.py
    """
    for edge in generator():
        if(edge[0] == i1 and edge[1] == i2):
            return True
        if(edge[0] == i2 and edge[1] == i1):
            return True
    return False

def get_vertex_closest(x, y, id_list) -> Vertex:
    """
    Finds vertex closest to provided x, y
    """
    dist_list = [((vert.x - x)**2 + (vert.y - y)**2, vert) for vert in [find_vertex_with_id(v) for v in id_list]] 
    def sort_key(e):
        return e[0]
    dist_list.sort(key=sort_key)
    return dist_list[0][1]
        
def P9(i1, i2, i3, i4):
    """
    i1 and i2 share 1 E node, which needs to be mergd with another    \n                                     
    i1 and i2 share 1 i node, from lower layer                        \n                 
    i3 and i4 share 1 E node, which needs to be mergd with another    \n                                     
    i3 and i4 share 1 i node, from lower layer                        \n                 
    i1 and i3 share 1 E node                                          \n 
    i2 and i4 share 1 E node                                            
    """
    global vertices_graph_fragment
    global graph_fragment_list
    #find_vertex_with_id(20).label = VertexLabel.E

    ### TEST HORIZONTAL
    merge_vertices([32, 46])    # ONLY FOR TESTS!!    
    merge_vertices([44,58])     # ONLY FOR TESTS!!
    
    #vertices_graph_fragment[35].edges.remove((32, 34))
    ### TEST VERTICAL
    #merge_vertices([38,46])    # ONLY FOR TESTS!!    
    #merge_vertices([44,52])     # ONLY FOR TESTS!!
    # basic requirements check
    shared_i12_list = find_shared_connected_node(i1, i2, yield_layer_connections_edges)
    if(len(shared_i12_list) != 1):
        raise ValueError()

    shared_i34_list = find_shared_connected_node(i3, i4, yield_layer_connections_edges)
    if(len(shared_i34_list) != 1):
        raise ValueError()
    shared_i12 = shared_i12_list[0]
    shared_i34 = shared_i34_list[0]

    shared_i12v : Vertex = find_vertex_with_id(shared_i12)
    shared_i34v : Vertex = find_vertex_with_id(shared_i34)

    if(shared_i12v.label != VertexLabel.i):
        raise ValueError()
    if(shared_i34v.label != VertexLabel.i):
        raise ValueError()

    shared_i1234 = find_shared_connected_node(shared_i12, shared_i34, yield_fragment_edges)
    if(len(shared_i1234) == 0):
        raise ValueError()

    shared_i1234v : Vertex = find_vertex_with_id(shared_i1234[0])
    if(shared_i1234v.label != VertexLabel.E):
        raise ValueError()

    # find both E nodes shared between 2 sides
    shared_e13_list = find_shared_connected_node(i1, i3, yield_fragment_edges)
    if(len(shared_e13_list) != 1):
        raise ValueError()
    shared_e13 : Vertex = find_vertex_with_id(shared_e13_list[0])
    if(shared_e13.label != VertexLabel.E):
        raise ValueError()
    shared_e24_list = find_shared_connected_node(i2, i4, yield_fragment_edges)
    if(len(shared_e24_list) != 1):
        raise ValueError()
    shared_e24 : Vertex = find_vertex_with_id(shared_e24_list[0])
    if(shared_e24.label != VertexLabel.E):
        raise ValueError()

    # no edge between those 2 
    if(edge_exists(shared_e24.id, shared_e13.id, yield_all_edges)):
        raise ValueError()

    # find coordinates
    x1 = shared_e13.x
    y1 = shared_e13.y
    x2 = shared_e24.x
    y2 = shared_e24.y
    
    merge_x = (x1+x2)/2
    merge_y = (y1+y2)/2

    # find both E nodes which need to be merged
    merge_e12_list = find_shared_connected_node(i1, i2, yield_fragment_edges)
    merge_e12 = get_vertex_closest(merge_x, merge_y, merge_e12_list)
    if(merge_e12.label != VertexLabel.E):
        raise ValueError()

    merge_e34_list = find_shared_connected_node(i3, i4, yield_fragment_edges)
    merge_e34 = get_vertex_closest(merge_x, merge_y, merge_e34_list)
    if(merge_e34.label != VertexLabel.E):
        raise ValueError()

    if(not edge_exists(shared_e24.id, merge_e12.id, yield_all_edges)):
        raise ValueError()
    if(not edge_exists(shared_e24.id, merge_e34.id, yield_all_edges)):
        raise ValueError()

    if(not edge_exists(shared_e13.id, merge_e12.id, yield_all_edges)):
        raise ValueError()
    if(not edge_exists(shared_e13.id, merge_e34.id, yield_all_edges)):
        raise ValueError()

    if(edge_exists(merge_e34.id, merge_e12.id, yield_all_edges)):
        raise ValueError()

    mergedID = min(merge_e12.id, merge_e34.id)
    merge_vertices([merge_e12.id, merge_e34.id])

    merged : Vertex = find_vertex_with_id(mergedID)
    merged.x = merge_x
    merged.y = merge_y

    changed_vertex = []
    for vertex in yield_all_vertices():
        if vertex.y <= -6 and vertex.y >= -8 and vertex.id not in changed_vertex:
            vertex.y -= 1
        if vertex.x > 2 and vertex.id not in changed_vertex:
            vertex.x -= 1
        changed_vertex.append(vertex.id)

