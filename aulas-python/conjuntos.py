numeros = [1, 3, 5, 3, 8, 1]
conjunto = set(numeros)
print(conjunto)
numeros = list(conjunto)
print(numeros)
print(numeros[0])

#Para acessarmos os indices em conjuntos

carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

