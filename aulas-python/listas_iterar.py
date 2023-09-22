carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

#Função enumerate (qujando queremos saber o indice)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")