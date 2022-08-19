
class Node:
    def __init__(self, valor):
        self.valor =  valor
        self.next = None
        
class Lista:
    def __init__(self):
        self.head = None
        
    def insert_head(self, valor): #Inserindo um novo elemento no inicio da lista
        new_node = Node(valor)
        new_node.next = self.head
        self.head = new_node
        return ' valor inserido com sucesso '
    
    def insert_end(self, valor): #Inserindo valor no fim 
        new_node = Node(valor)
        new_node.next = self.head
        self.head = new_node
    
    def insert(self, valor, posição): #Inserir elemento em uma determinada posição
        new_node = Node(valor)
        i = 0
        anterior = None
        atual = self.head
        while anterior and i < posição:
            anterior = atual
            atual = atual.next
            i += 1
        if anterior:
            anterior.next = new_node
        new_node.next = atual 
        if i == 0:
            self.head = new_node
        
    def find(self, valor):# Verificar se um elemento está na lista
        encontrado = False
        node = self.head
        while node and not encontrado:
            if node.valor == encontrado:
               encontrado = True
            node = node.next
        return encontrado
    
    def remove_head(self): # Remove do começo da lista(head, cabeça) e retorna o valor
        if self.head: # para evitar erro se caso a lista encadeada esteja vazia
            node = self.head
            self.head = node.next
            return node.valor
        
    def remove_end(self):  # Remove o último elemento e retorna o seu valor
        if self.head:
            if self.head.next:
                node = self.head
                while node.next.next:
                    node = node.next
                end = node.next
                node.next = None
                return end.valor
            else:
                end = self.head
                self.head = None
                return end.valor
    def remove_valor(self, valor): # Remove elemento com determinado valor
        if self.head:
            anterior = None
            atual = self.head
            while atual and atual.valor != valor:
                anterior = atual
                atual = atual.next
            if atual:
                node = atual
                if anterior:
                    anterior.next = atual.next
                else:
                    self.head = atual.next
                return node.valor
            
    def __str__(self): # imprime os valores da lista
        s = ''
        node = self.head
        while node:
            s += '{} ->'.format(node.valor)
            node = node.next
        if s:
            return s
        else:
            return ' Lista Vazia'
        
    def apaga_lista(self):
        while self.head != None:
            self.remove_head()
        return ' Lista apagada com sucesso! '