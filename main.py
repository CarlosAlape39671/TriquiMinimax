from interfaz.interface import Interfaz
from movimientos import Movimientos
# from nodos.tableroNode import TableroNode

class Main():
    def __init__(self):
        interface = Interfaz()
        # self.funcionParaPruebas()
    
    def funcionParaPruebas(self):
        # 1 = x
        # 0 = o
        # None = vacio
        root = [[1,0,0],[1,None,None],[0, 1, None]]
        # root = [[1,0,0],[1,None, None],[0, 1, None]]
        a = Movimientos(root, 1)
        rootNode = a.getRootNode()
        # print(rootNode)
        # print(rootNode.root_node.nodos)
        # print(rootNode.root_node.nodos[0].nodos)
        # print(rootNode.root_node.nodos[0].nodos[0].nodos)
        print("----------------------------------------------")
        print(rootNode.root_node.nodos[0].estado)
        # print(rootNode.root_node.nodos[0].nodos[1].nodos[0].estado)
        # print(rootNode.root_node.nodos[1].nodos[0].nodos[0].estado)
        # print(rootNode.root_node.nodos[1].nodos[1].nodos[0].estado)
        # print(rootNode.root_node.nodos[2].nodos[0].nodos[0].estado)
        # print(rootNode.root_node.nodos[2].nodos[1].nodos[0].estado)
        print("----------------------------------------------")
        # print(rootNode.root_node.nodos[0].nodos[0].estado)
        # print(rootNode.root_node.nodos[0].nodos[1].estado)
        # print(rootNode.root_node.nodos[1].nodos[0].estado)
        # print(rootNode.root_node.nodos[1].nodos[1].estado)
        # print(rootNode.root_node.nodos[2].nodos[0].estado)
        # print(rootNode.root_node.nodos[2].nodos[1].estado)

        # print(rootNode.root_node.puntuacion)
        # print(rootNode.root_node.nodos[0].estado)
        # print(rootNode.root_node.nodos[0].puntuacion)
        # print(rootNode.root_node.nodos[0].nodos[0].estado)
        # print(rootNode.root_node.nodos[0].nodos[0].puntuacion)
        # print(rootNode.root_node.nodos[0].nodos[0].nodos[0].estado)
        # print(rootNode.root_node.nodos[0].nodos[0].nodos[0].puntuacion)
        
        print(a.getEvaluacion())
        print(rootNode.root_node.estado)
        print(rootNode.root_node.puntuacion)
        print(rootNode.root_node.nodos[0].estado)
        print(rootNode.root_node.nodos[0].puntuacion)
        print(rootNode.root_node.nodos[0].nodos[0].estado)
        print(rootNode.root_node.nodos[0].nodos[0].puntuacion)
        print(rootNode.root_node.nodos[0].nodos[0].nodos[0].estado)
        print(rootNode.root_node.nodos[0].nodos[0].nodos[0].puntuacion)
        # print(a.getEvaluacion())
        # nodo = [[1,None,None],[None,None, None],[0, 1, None]]
        # node = TableroNodeRoot(nodo)
        # a.puntuacion(node.root_node, 1)
        # print(node.root_node.puntuacion)
    
        # print(a.ganador(root))    
        
    
    
a = Main()