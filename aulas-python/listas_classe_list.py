""" [].append - Inclui um objeto na lista (ultima posição)
lista = []
lista.append(1)
lista.append("Python")
lista.append([40,30,20])

lista2 = []
[].clear - Deleta todos os objetos da lista
lista2.clear()
print(lista)

[].copy - Faz uma cópia em outro endereço de memória
lista2 = [1, "Python", [40,30,20]]
l2 = lista.copy()
print(l2)"""

#[].count - conta quantas vezes um determinado objeto pertence a lista
cores = ["vermelho", "azul", "verde", "amarelo"]

"""print(cores.count("vermelho"))
print(cores.count("azul"))
print(cores.count("verde"))

#[].extende - juntas as listas
lista2 = [1, "Python", [40,30,20]]

cores.extend(lista2)
print(cores)

#[].index - verificar a posição na lista
print(cores.index("verde"))

#[].pop - comportamento de uma "pilha" remove do ultimo para o primeiro
print(cores.pop())
print(cores.pop())
print(cores)
#[].remove - retira o objeto especifico

cores.remove("vermelho")
print(cores)"""

#[].reverse - retorna a lista espelhada
cores.reverse()
print(cores)

#[].sort - ordena em ordem alfabetica (padrão) porém há alguns parametros
# reverse = TRUE - retorna a lista espelhada
#key=lambda X:len(x) - retorna a lista de acordo com a quantidade de caracteres
#key=lambda X:len(x), reverse=True - retorna a funcão acima espelhada
cores.sort()

 [n**2 if n > 6 else n for n in range(10) if n % 2 == 0]





