from enum import Enum

class VertexLabel(Enum):
    """
    This Enumerator represents a vertix label
    E - an "edge" vertex from which you cannot make any lower part of the graph
    I - a middle vertex from which you can make a lower part of the graph
    i - a middle vertex from which you cannot make a lower part of the graph as it has already been built
    """
    E = 1
    I = 2
    i = 3
    UNDEFINED = 4


class Vertex:
    """
    This class represents a vertex. It has its coordinates (x, y), unique id and label (from VertexLabel enum).
    """
    def __init__(self, x, y, id, label):
        self.x = x
        self.y = y
        self.id = id
        self.label = label

