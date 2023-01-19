class GraphFragment:
    '''
    This class represents a graph fragment - the fragment of graph identified with a vertex from which we can build more graph
    fragments on lower layers. This is a middle_vertex (as mostly this vertex is in the middle of graph fragment).
    For productions P1 to P6 and P10 you use only one graph fragment in the left side of production.
    For other productions you need to choose 2 or more graph fragments by middle vertices for the left side of production,
    choose desired vertices, merge them and modify graph fragments to be updated as merged at the graph fragment list.

    Squares are the physical 1x1 squares which the fragment occupies.
    '''
    def __init__(self, squares, vertices, layer_number, edges, middle_vertex):
        self.squares = squares
        self.vertices = vertices
        self.layer_number = layer_number
        self.edges = edges
        for i in range(len(self.edges)):
            self.edges[i] = (min(self.edges[i][0], self.edges[i][1]), max(self.edges[i][0], self.edges[i][1]))

        self.middle_vertex = middle_vertex

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"<Graph Fragment: (squares: {self.squares}, vertices: {self.vertices}, layerNumber: {self.layer_number}, middle_vertex={self.middle_vertex})>\n"
