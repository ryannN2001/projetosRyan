import Fila 
fila = Fila.Fila()
print('+-+'*12)
print(" Menu da Lista")
print('+-+'*12)


print("- Digite 1 para adicionar um item na Fila", 
      "\n- Digite 2 para encontrar a posição de um elemento dentro da fila", 
      "\n- Digite 3 para buscar um determinado elemento na fila", "\n- Digite 4 para remover um elemento da fila", 
      "\n- Digite 5 para apagar fila")
print('+-+'*12)

opção = int(input(" Digite uma opção desejada: "))

if opção == 1:
   valor = int(input("digite um valor: "))
   print(fila.insert(valor))
elif opção == 2:
   valor = int(input(" Digite uma posição para encontrar o elemento: "))
   print()
      Pass
      
elif opção == 3:
      valor = int(input(" digite um numero para buscar um determinado elemento a fila: "))
      print()
      pass
    
elif opção == 4:
      print(fila.remove())
      Pass
  
elif opção == 5:
      print(fila.apaga_lista())
      
else:
  print(" Digite uma opção válida! ")
