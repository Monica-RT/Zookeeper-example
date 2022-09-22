from turtle import onscreenclick
from treelib import Node,Tree

class Ztree:
    def __init__(self):
        self.tree = Tree()
        self.tree.create_node("/","/")
    
    def get_tree(self):
        return self.tree
#creacion de nodos. En caso de ser efimero, se asigna un tiempo de vida. En caso contrario, el valor de vida asignado sera None
    def create(self,path,data,ephemeral,OnService,timeDead,parent):
        
        if(ephemeral):
            self.tree.add_node(Node(path,path,data= Znode(path,data,ephemeral,OnService,timeDead)),parent= parent) 
        else:
            self.tree.add_node(Node(path,path,data= Znode(path,data,ephemeral,OnService,None)),parent= parent)
#Funcion para eliminar nodos. Se corrobora la existencia del nodo solicitado
#En caso de que la version del nodo no coincida, se genera un mensaje de error
#En caso de que el nodo sea efimero, se imprime el tiempo de vida restante hasta que se elimina
#En caso de que el nodo no este en servicio y sea efimero, se elimina (simulando la caida de un servidor)
    def delete(self,path,version):
        if(self.exist(path)):
            nodo = self.tree.get_node(path)
            nodoData = nodo.data
            if(nodoData.ephemeral == False):
                if(self.tree.contains(path)):
                    if(nodoData.version == version):
                        self.tree.remove_node(path)
                    else:
                        print("Las versiones no concuerdan c:")
            else:
                if((nodoData.OnService == False) and (nodoData.ephemeral == True)):
                    self.tree.remove_node(path)
                    return 0
                else:
                    if((nodoData.OnService == True) and (nodoData.ephemeral == True)):
                        for i in range(nodoData.timeDead,-1,-1):
                            if(i == 0):
                                if(nodoData.version == version):
                                    self.tree.remove_node(path)
                                else:
                                    print("Las versiones no concuerdan c:")
                            else:
                                print("Tiempo restante de vida = {i}".format(i=i))
        else:
            print("Nodo no existe")
    #Busca un nodo a partir de su ruta, retornando True si existe y False si no        
    def exist(self,path):
        if(self.tree.contains(path)):
            return True
        else: 
            return False
    #Se imprime todo el arbol 
    def showTree(self):
        print("\t\t -------Estado actual del Arbol--------")
        self.tree.show()
    #Se verifica que nodo solicitado exista
    #En caso afirmativo, se muestran el contenido del nodo
    def getData(self,path):
        if(self.exist(path)):
            nodo = self.tree.get_node(path)
            nodoData = nodo.data
            return(nodoData.data)
        else:
            print("Nodo no existe")
    #Se verifica la existencia del nodo solicitado
    #Se cambia el contenido del nodo por el ingresado 
    def setData(self,path,contenido):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            nodo = nodotemp.data
            nodo.data = contenido
            nodo.version = nodo.version + 1
        else:
            print("Nodo no existe")
    #Se verifica la existencia del nodo solicitado
    #En caso afirmativo, se muestra el path del nodo, la version, el contenido y si es efimero o no
    def showNode(self,path):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            nodo = nodotemp.data
            nodo.get_node_info()
        else:
            print("Nodo no existe")
    #Se verifica la existencia del nodo solicitado
    #En caso afirmativo, se obtienen los hijos inmediatos del nodo solicitado
    def getChildren(self,path):
        if(self.exist(path)):
            nodotemp = self.tree.get_node(path)
            print(self.tree.children(path))
        else:
            print("Nodo no existe")
    

    



#Definicion de la clase Znode con sus funciones y atributos
class Znode:
    def __init__(self,path,data,ephemeral,OnService,timeDead):
        self.path = path
        self.ephemeral = ephemeral
        self.data = data
        self.node = Node(path,path)
        self.OnService = OnService 
        self.timeDead = timeDead
        self.version = 0
    
    def get_node_info(self):
        print("\t \t------ZNode information--------\t\t \n")
        print("Path = {path} ".format(path = self.path))
        print("Ephemeral = {ephemeral} ".format(ephemeral = self.ephemeral))
        print("Version = {version} ".format(version = self.version))
        print("Data = {data} ".format(data = self.data))

        
        
        
        
