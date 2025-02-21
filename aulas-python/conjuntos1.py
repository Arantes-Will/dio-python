#Estrutura de dados set -> um set é uma coleção de objetos repetidos, representação de conjuntos matemáticos ou eliminação de itens duplicados

print(set([1,2,3,1,3,4]))
print(set('abacaxi'))
print(set(('palio','gol','celta','palio'))) #Nem sempre o set te devolve o conjunto na ordem
#Conjuntos não suportam indexação e nem fatiamento então precisamos converter o set para uma lista

numeros = {1,2,3,2}
print(numeros)

numeros = list(numeros)
print(numeros)
print(numeros[0])

#Métodos da classe set (conjuntos matemáticos)
conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.union(conjunto_b)) #União de conjuntos
print(conjunto_a.intersection(conjunto_b))#Intersecção de conjuntos
print(conjunto_a.difference(conjunto_b)) #Diferença de conjuntos
print(conjunto_a.symmetric_difference(conjunto_b)) #Diferença simetrica (Todos os elementos que não estao na intersecção)
print(conjunto_a.issubset(conjunto_b)) #Verifica se um é subconjunto do outro
print(conjunto_a.issuperset(conjunto_b)) 
print(conjunto_a.isdisjoint(conjunto_b)) #Verifica se conjuntos disjuntos


#Método .add inclui um elemento
#. clear - > limpar o conjunto
#. copy -> gerar uma cópia do conjunto
# .discard -> descartar um valor numeros.discard(1)
# .pop -> eliminar valores do conjunto a partir do primeiro elemento
# .remove -> elimina um elemento especifico
# .len -> tamanho do conjunto

#O operador in verifica se o elemento está no conjunto


