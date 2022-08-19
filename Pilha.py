class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0

    
    def insere(self, elem): #insere elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        return ' elemento inserido com sucesso '
    
    def pop(self): #remove o elemento do topo
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size -1
            return node.data
        return ' pilha vazia '
    
    def peek(self): # retorna o topo sem remover
           if self._size > 0:
            return self.top.data
           return ' pilha vazia '
       
    def __len__(self): # ler o elementos na pilha
        
        r =''
        pointer = self.top #variavél pointer é o ponteiro 
        while(pointer):
            r = r + str(pointer.data) + " \n "
            pointer = pointer.next
        return r
    
    def __str__(self): #mostrar os elementos para o usuário
        return self.__repr__()
    
    def apaga_lista(self):
        while self.top != None:
            self.remove_top()
        return ' Lista apagada com sucesso! '
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    