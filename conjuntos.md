## 💻 Conjuntos em Python (sets)


Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens
duplicados de um iterável.
OBS: Conjuntos não garantem elementos organizados

```
set([1,2,3,1,3,4]) #{1,2,3,4}
set("abacaxi") # {"b","a","c","x","i"}

```

#### Acessando os dados
Conjuntos em Python não suportam indexação e nem fatiamento, caso queira acessar os valores é necessario converter o conjunto
para lista.

```
numeros = {1,2,3,2}
numeros = list(numeros)
print(numeros[0])
```

Para iteração utilizamos o laço for, e caso queiramos saber o indice do objeto dentro do laço for podemos usar a função
enumerate.

```
carros = {"gol", "celta", "palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
``` 

#### Métodos da classe set
```
#Lembramos da teoria de conjuntos e suas propriedades
conjunto1.union(conjunto2) # União
conjunto1.intersection(conjunto2) #Intersecção
conjunto2.difference(conjunto1) #Diferença
conjunto1.symmetric_difference(conjunto2) #Diferença Simétrica
conjunto1.issubset(conjunto2) #Verificamos se os elementos de um estão no outro conjunto (retorna True ou False)
conjunto2.issuerset(conjunto1) #Verificamos um conjunto é subconjunto do outro (retorna True ou False)
conjunto1.isdisjoint(conjunto2) #Conjunto disjunto (retorna True ou False)
{}.add #Se um elemento não existir no conjunto ele é adicionado
{}.clean #Elimina os elementos do conjunto
{}.copy # Faz a cópia do conjunto
{}.discard # Elimina um elemento especifico
{}.pop # Elimina o elemento um por um da esquerda para a direita
{}.remove #Elimina um elemento que existe no conjunto
len() # numero de elementos (descarta os repetidos)
in #verifica se aquele elemento pertence ao conjunto (retorna True ou False) 1 in numeros por exemplo
```

## 💻 Dicionários

Um dicionário é um conjunto não-ordenado de pares chave:valor, onde as chaves são únicas em uma dada instancia do dicionário.
Dicionários são delimitados por chaves: {}, contém uma lista de pares chave:valor separada por vírgulas.

```
pessoa = {"nome": "William", "idade":28}
pessoa = dict(nome = "William", idade=28)
pessoa["telefone"] = "3333-1234"

```

#### Dicionários aninhados
Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável
como (strings e números)

```
contatos = {
    "williamarantes.tec@gmail.com": {"nome": "William", "telefone": "3334-1234"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "4578-6541",}
}

```

#### Iteração
```
for chave in contatos:
    print(chave, contatos[chave])


for chave, valor in contatos.items():
    print(chave,valor)

```

#### Métodos da classe dict

```
contatos = {
    "williamarantes.tec@gmail.com": {"nome": "William", "telefone": "3334-1234"},
    "fernanda@gmail.com": {"nome": "Fernanda", "telefone": "4578-6541",}
}

contatos.clear() # apaga todos os valores do dicionário
contatos.copy() #copia do nosso dicionário
{}.fromkeys(["nome","telefone"]) #Cria a chave #{"nome: None, "telefone": None
contatos.get() / contatos.get("chave", {})
contatos.items() # retorna uma tupla com chave e valor
contatos.keys() #retorna somente as chaves
contatos.pop() #remove uma chave do dicionário
contatos.popitem() #remove os itens na sequência
contatos.setdefault() #se o atributo não estiver no dicionario ele adiciona, se estiver retorna o valor e não o altera
contatos.update() #atualiza o dicionario com outro dicionário
contatos.values() #retorna todos os valores do dicionário
in #Retora True ou False 
del #outra forma de tirar o elemento

```














