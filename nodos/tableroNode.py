class TableroNode:

    def __init__(self, estado, puntuacion = 0):
        self.estado = estado
        self.puntuacion = puntuacion
        self.nodos = []
    
    def new_child_node(self, nodo):
        self.nodos.append(nodo)
        pass