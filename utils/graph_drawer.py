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


def draw_graph():
    '''
    Function for graphically present generated graphs
    '''
    global color_list
    G = nx.Graph()
    for graph_fragment in graph_fragment_list:
        for vertex in graph_fragment.vertices:
            if G.nodes.get(vertex.id) is None:
                G.add_node(vertex.id)
                color_list.append(label_color_map[vertex.label])
    for graph_fragment in graph_fragment_list:
        for edge in graph_fragment.edges:
            G.add_edge(edge[0], edge[1])
    for inter_layer_connection in inter_layer_connections:
        G.add_edge(inter_layer_connection[0], inter_layer_connection[1])
    pos = {}
    for graph_fragment in graph_fragment_list:
        for vertex in graph_fragment.vertices:
            if vertex.x > 2 and vertex.y < -8:
                pos[vertex.id] = (vertex.x-1, vertex.y)
            elif vertex.y < -5 and vertex.y > -9 and vertex.x < 3:
                pos[vertex.id] = (vertex.x, vertex.y-1)
            elif vertex.y < -5 and vertex.y > -9 and vertex.x > 2:
                pos[vertex.id] = (vertex.x-1, vertex.y-1)
            else:
                pos[vertex.id] = (vertex.x, vertex.y)
    nx.draw_networkx(G, pos, node_color=color_list)  # , node_size = 10, font_size=1)
    ax = plt.gca()
    plt.axis("off")
    plt.show()
