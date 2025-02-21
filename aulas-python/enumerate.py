#quando preciso saber o indice do elemento a qual estou percorrendo utilizamos o enumerate
#neste exemplo estamos usando conjuntos

carros = {'palio','gol','celta'}

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')