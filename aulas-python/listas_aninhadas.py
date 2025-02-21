#Listas podem armazerar todos os tipos de objetos Python, portanto podemos ter listas que armazenam outras listas. 
#Exemplo: Representação de matrizes

matriz = [
    [1, 'a', 2],
    ['b', 3, 4],
    [6, 5, 'c']
]

print(matriz) #Toda a matriz
print(matriz[0]) #[1, 'a', 2]
print(matriz[0][0]) #1
print(matriz[0][-1]) #2
print(matriz[-1][-1]) #c

