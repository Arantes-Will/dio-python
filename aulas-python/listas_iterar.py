numeros = [1,30,21,2,9,65,34]
pares = []
quadrado = []

#for numero in numeros:
    #print(numero)

#Compressão de listas -> oferece uma sintaxe mais curta quando você deseja: criar uma nova lista com base nos valores de uma lista
#existente (filtro) ou gerar uma nova lista aplicando alguma modificação nos elementos de uma lista existente.

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)

print(pares)

#Comprssão de listas
        #retorno ----- iteração ----- filtro -----------
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)