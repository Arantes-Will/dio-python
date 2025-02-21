#Extrair um conjunto de valores de uma sequência

lista = ['P','y','t','h','o','n']
print(lista)

print(lista[2:]) #Inclui o 't'
print(lista[:2]) #Não inclui o t
print(lista[1:3]) #Inclui o y e exclui o h
print(lista[0:3:2]) #[0:3] -> ['P','y','t']
print(lista[::]) #Tudo
print(lista[::-1]) #Invertido