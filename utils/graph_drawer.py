import math
import networkx as nx
import matplotlib.pyplot as plt
from utils.common import graph_fragment_list, inter_layer_connections
from utils.vertex import VertexLabel

label_color_map = {
    VertexLabel.E: '#00B3FF',
    VertexLabel.I: 'orange',
    VertexLabel.i: 'red'
}
color_list = []  # empty color list to store color value for each graph 
position_move = False

def set_position_move(val):
    global position_move
    position_move = val

def draw_graph(inter_layer = False):
    '''
    Function for graphically present generated graphs
    '''
    global color_list
    global position_move
    color_list.clear()
    G = nx.Graph()
    for graph_fragment in graph_fragment_list:
        for vertex in graph_fragment.vertices:
            if G.nodes.get(vertex.id) is None:
                G.add_node(vertex.id)
                color_list.append(label_color_map[vertex.label])
    for graph_fragment in graph_fragment_list:
        for edge in graph_fragment.edges:
            assert(edge[0] < edge[1])
            G.add_edge(edge[0], edge[1])
    if(inter_layer):
        for inter_layer_connection in inter_layer_connections:
            G.add_edge(inter_layer_connection[0], inter_layer_connection[1])
    pos = {}
    for graph_fragment in graph_fragment_list:
        for vertex in graph_fragment.vertices:
            pos[vertex.id] = (vertex.x, vertex.y)

    if(position_move):
        for graph_fragment in graph_fragment_list:
            for edge in graph_fragment.edges:
                assert(edge[0] < edge[1])
                dX = pos[edge[0]][0] - pos[edge[1]][0]
                dY = pos[edge[0]][1] - pos[edge[1]][1]
                dX /= math.sqrt(dX*dX + dY * dY)
                dX /= 9
                dY /= math.sqrt(dX*dX + dY * dY)
                dY /= 9
                pos[edge[0]] = (pos[edge[0]][0] - dX, pos[edge[0]][1] - dY)
                pos[edge[1]] = (pos[edge[1]][0] + dX, pos[edge[1]][1] + dY)

    nx.draw_networkx(G, pos, node_color=color_list)  # , node_size = 10, font_size=1)
    ax = plt.gca()
    plt.axis("off")
    plt.show()
