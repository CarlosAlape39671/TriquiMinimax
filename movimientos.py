from nodos.tableroNodeRoot import TableroNodeRoot
from nodos.tableroNode import TableroNode
import copy

class Movimientos:
    def __init__(self, tableroRoot, player):
        self.rootNode = TableroNodeRoot(tableroRoot)
        self.player = player 
        self.puntuacion(self.rootNode.root_node, self.player)
        nivel = 0
        if player == 1:
            self.rootNode.root_node.jugador = 0
        else:
            self.rootNode.root_node.jugador = 1
        self.evaluacion = self.generarMovimientos(self.rootNode.root_node, self.player, nivel)
        
    def generarMovimientos(self, root, player, nivel):
        # Evalua si el tablero está lleno o hay un ganador o si se llegó al nivel 5
        lleno = True
        for fila in root.estado:
            if None in fila:
                lleno = False
        ganador = self.ganador(root.estado)
        if lleno or ganador != None or nivel == 5:
        # if lleno or ganador != None:
            root.evaluacion = root.puntuacion
            return root.puntuacion
        
        # Genera los nodos hijos con el nuevo estado del tablero
        for i in range(len(root.estado)):
            fila = root.estado[i]
            if None in fila:
                for j in range(len(fila)):
                    elemento = root.estado[i][j]
                    if elemento == None:
                        # genera una copia del tablero
                        nuevoTablero = copy.deepcopy(root.estado)
                        nuevoTablero[i][j] = player
                        # crea el nodo
                        nodo = TableroNode(nuevoTablero)
                        # da la puntuacion al nodo
                        self.puntuacion(nodo, player)
                        nodo.jugador = player
                        # agrega el nodo al root
                        root.new_child_node(nodo)
        
        # llamada recursiva
        puntuaciones = []
        for nodo in root.nodos:
            if player == 1:
                oponentPlayer = 0
            else:
                oponentPlayer = 1
            puntaje = self.generarMovimientos(nodo, oponentPlayer, nivel + 1)
            puntuaciones.append(puntaje)
        
        puntuacionRetornar = puntuaciones[0]
        for puntuacion in puntuaciones:
            if player == 1 and puntuacion > puntuacionRetornar:
                puntuacionRetornar = puntuacion
            elif player == 0 and puntuacion < puntuacionRetornar:
                puntuacionRetornar = puntuacion
        root.evaluacion = puntuacionRetornar
        return puntuacionRetornar
    
    # da la puntuacion a un nodo
    def puntuacion(self, nodo, player):
        ganador = self.ganador(nodo.estado)
        if ganador != None:
            if ganador == 1:
                nodo.puntuacion = 10
            elif ganador != 1:
                nodo.puntuacion = -10
        else:
            if self.tableroLleno(nodo.estado):
                nodo.puntuacion = 0
            else:
                if self.esPosibleGanadorConDosEnLinea(nodo.estado, 0):
                    if player == 1:
                        nodo.puntuacion = -5
                    else: 
                        nodo.puntuacion = 5
                else:
                    if self.esPosibleGanadorConDosEnLinea(nodo.estado, 1):
                        if player == 1:
                            nodo.puntuacion = 5
                        else:
                            nodo.puntuacion = 5
                    else:
                        nodo.puntuacion = 0
                            
    # verifica si el tablero está lleno
    def tableroLleno(self, tablero):
        for fila in tablero:
            if None in fila:
                return False
        return True
                        
    # verifica un tres en linea
    def ganador(self, tablero):
        for i in range(3):
            # Lineas horizontales
            if tablero[i][0] == tablero[i][1] == tablero[i][2]:
                return tablero[i][0]
            # Lineas verticales
            if tablero[0][i] == tablero[1][i] == tablero[2][i]:
                return tablero[0][i]
            
        # Diagonales
        if tablero[0][0] == tablero[1][1] == tablero[2][2]:
            return tablero[1][1]
        if tablero[0][2] == tablero[1][1] == tablero[2][0]:
            return tablero[1][1]
        else:
            return None
                                    
    # verifica si un jugador es posible ganador con dos en linea
    def esPosibleGanadorConDosEnLinea(self, tablero, player):
        
        for i in range(3):
            # Lineas horizontales
            if ((tablero[i][0] == tablero[i][1] == player and tablero[i][2] == None)
                or (tablero[i][0] == tablero[i][2] == player and tablero[i][1] == None)
                or (tablero[i][1] == tablero[i][2] == player and tablero[i][1] == None)):
                return True
            # Lineas verticales
            if ((tablero[0][i] == tablero[1][i] == player and tablero[2][i] == None)
                or (tablero[0][i] == tablero[2][i] == player and tablero[1][i] == None)
                or (tablero[1][i] == tablero[2][i] == player and tablero[0][i] == None)):
                return True
            
        # Diagonales
        if ((tablero[0][0] == tablero[1][1] == player and tablero[2][2] == None)
            or (tablero[0][0] == tablero[2][2] == player and tablero[1][1] == None)
            or (tablero[1][1] == tablero[2][2] == player and tablero[0][0] == None)):
            return True
        if ((tablero[0][2] == tablero[1][1] == player and tablero[2][0] == None)
            or (tablero[0][2] == tablero[2][0] == player and tablero[1][1] == None)
            or (tablero[1][1] == tablero[2][0] == player and tablero[0][2] == None)):
            return True
        else:
            return False
            
    def getRootNode(self):
        return self.rootNode
    
    def getEvaluacion(self):
        return self.evaluacion