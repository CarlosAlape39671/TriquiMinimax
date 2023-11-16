class TableroNode:

    def __init__(self, estado, puntuacion = 0, evaluacion = 0, jugador = None):
        self.estado = estado
        self.puntuacion = puntuacion
        self.evaluacion = evaluacion
        self.jugador = jugador
        self.nodos = []
    
    def new_child_node(self, nodo):
        self.nodos.append(nodo)