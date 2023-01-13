class Square:
    """
    This clas represents a single (indivisible) 1x1 square
    Field id is not the same as vertice id. Vertice id is unique in the whole graph and field id identifies each square within
    a layer - on layer 0 you have 1 square with field id 0, on layer 1 you have 4 squares with field ids 0-3, on layer 2 you have
    16 squares with field ids 0-15 and so on...
    """
    def __init__(self, field_id, layer_number):
        self.field_id = field_id
        self.layer_number = layer_number
        self.vertices = []

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"<Square: (Field: {self.field_id}, layer: {self.layer_number}, vertices: {self.vertices})>\n"
