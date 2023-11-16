from interfaz.interface import Interfaz
from movimientos import Movimientos
import json
# from nodos.tableroNode import TableroNode

class Main():
    def __init__(self):
        # interface = Interfaz()
        self.funcionParaPruebas()
    
    def funcionParaPruebas(self):
        # 1 = x
        # 0 = o
        # None = vacio
        root = [[None,1,0],[0,1,1],[None, None, 0]]
        # root = [[1,0,0],[1,None, None],[0, 1, None]]
        a = Movimientos(root, 1)
        rootNode = a.getRootNode()
        
        print(rootNode)
        # diccionario = vars(rootNode.root_node)
        rootNodeToDictionary = self.recorrer(rootNode.root_node)
        
        # Convierte el diccionario a una cadena JSON con indentación de 2 espacios
        cadena_json = json.dumps(rootNodeToDictionary, separators=(',', ':'), indent=2, ensure_ascii=False)
        
        # Especifica la ruta del archivo donde deseas guardar el JSO
        ruta_archivo = "semana_11/triqui/json/archivo.json"
        
        # Abre el archivo en modo escritura y sobrescribe su contenido con una cadena vacía
        with open(ruta_archivo, 'w') as archivo:
            archivo.write('')
    
        # Guarda la cadena JSON en el archivo
        with open(ruta_archivo, "w") as archivo:
            archivo.write(cadena_json)
        
    def recorrer(self, nodo):
        elementos = []
        diccionario = vars(nodo)
        n = []
        for linea in diccionario["estado"]:
            n.append(str(linea))
        diccionario["estado"] = n
        
        if len(nodo.nodos) == 0:
            return diccionario
        for nodo in nodo.nodos:
            diccionarioNodo = self.recorrer(nodo)
            elementos.append(diccionarioNodo)
        diccionario['nodos'] = elementos
        return diccionario
        
    
    
a = Main()