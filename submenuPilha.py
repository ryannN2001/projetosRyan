# sub menu de pilha

import Pilha
pilha = Pilha.Pilha()


print('+-+'*12)
print(" Menu da Lista")
print('+-+'*12)


print("- Digite 1 para adicionar um item na Fila", 
      "\n- Digite 2 para encontrar a posição de um elemento dentro da fila", 
      "\n- Digite 3 para buscar um determinado elemento na fila",
      "\n- Digite 4 para remover um elemento da fila", 
      "\n- Digite 5 para apagar fila")
print('+-+'*12)

opção = int(input(" Digite uma opção desejada: "))

if opção == 1:
    elem = int(input(" Digite um valor a ser adicionado na pilha: "))
    print(pilha.insere(elem))
    
elif opção == 2:
    valor = int(input("digite uma posição na qual você queira encontrar um elemento:"))
    print()
    
elif opção == 3:
    valor = int(input(" digite um determinado valor a ser procurado: "))
    print(pilha.__len__())
    
elif opção == 4:
    print(pilha.pop())

elif opção == 5:
    print(pilha.apaga_lista())
    
else:
    ("Digite uma opção válida!")