import Lista
lista = Lista.Lista()
print('+-+'*12)
print(" Menu da Lista")
print('+-+'*12)


print("- Digite 1 para adicionar item no início da lista","\n- Digite 2 para inserir um item no fim da lista","\n- Digite 3 para inserir em determinada posição",
      "\n- Digite 4 para encontrar um determinado item na Lista","\n- Digite 5 para buscar um elemento na Lista",
      "\n- Digite 6 para remover um elemento da Lista"," \n- Digite 7 para apagar a lista")  


opção = int(input(" Digite a opção desejada: ")) 
        
if opção == 1:
      valor = int(input(" Digite o valor a ser adicionado no inicio da lista: "))
      print(lista.insert_head(valor)) 
      
elif opção == 2:
      valor = int(input(" digite uma valor a ser adicionado: "))
      print(lista.insert_end(valor))
   
elif opção == 3:
      valor = int(input( " digite um valor para ser inserido em uma determinada posição: "))
      posição = int(input(" digite uma posição: "))
      print(lista.insert(valor, posição)) 
      
elif opção  == 4:
      valor = int(input(" Digite o valor a ser encontrado: "))
      print(lista.find(valor))
      
elif opção == 5:
      valor = int(input(" Digite um elemento a ser buscado na lista: "))
      print(lista.find(valor))
elif opção  == 6:
      
      valor = int(input(" Digite uma valor para ser removido: "))
      print(lista.remove_valor(valor))
    
elif opção  == 7:
      print(lista.apaga_lista())
    
else:
      print(" ERRO, Digite uma opção válida! ")