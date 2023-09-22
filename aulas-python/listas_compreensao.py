#Filtro versão 1
numeros = [1, 30, 2, 2, 9, 65, 34]
pares = []
quadrado = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


print(pares)
print()

pares = [numero for numero in numeros if numero % 2 == 0]
        #retorno ------ iteração -------condição------
print(pares)

## quero retornar meus números ao quadrado

quadrado = [numero ** 2 for numero in numeros]
print(quadrado)