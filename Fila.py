class Node:
    def __init__(self, dado = 0, proximo = None):
        self.dado = dado
        self.prox = proximo
    
    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)
    
class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        
    def __repr__(self):
        return "[" + str(self.first) + "]"
    
    def insert(self, novo):
        novo = Node(novo)
        if self.primeiro == None:
            self.ultimo = novo
        else:
            self.ultimo.proximo = novo
            self.ultimo = novo
    
    def remove(self):
        assert self.primeiro != None
        
        self.primeiro = self.primeiro.proximo
        if self.primeiro == None:
            self.ultimo = None
            
    def apaga_lista(self):
        while self.prox != None:
            self.remove_proximo()
        return ' Lista apagada com sucesso! '