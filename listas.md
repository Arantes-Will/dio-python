## 💻 Trabalhando com Listas em Python

#### Criação e acesso aos dados
Listas em Python podem armazenar de maneira sequencial qualquer tipo de objeto (mutáveis). Podemos criar listas utilizando:  
```
construtor list
função range
colocando valores separados por vírgula dentro de colchetes
```
Exemplos:
```
frutas = ["laranja" , "maca", "uva"]
frutas = []
letras = list("python")
numeros = list(range(10))
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
```
#### Acesso direto
Podemos acessar seus dados utilizando índices
```
frutas = ["laranja" , "maca", "uva"]
frutas[0] #laranja
frutas[1] #maca
frutas[-1] #uva
```

#### Listas aninhadas
Listas podem armazenar todos os tipos de objeto Python, portanto podemos ter listas que armazenam outras listas
```
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

matriz[0] #[1, "a", 2]
matriz[0][0] #1
matriz[0][-1] #2
matriz[-1][-1] # "c"
```

#### Fatiamento
```
lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] #["p", "y"]
lista[1:3] #["y", "t"]
lista[0:3:2] #["p", "t"]
lista[::] #["p", "y", "t", "h", "o", "n"]
lista[::-1] #["n", "o", "h", "t", "y", "p"]
```

#### Iterar listas
A forma mais comum para percorrer os dados de uma lista é utilizando o comando for.

```
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
```

#### Compreensão de listas
A compreesão de listas oferece uma sintaxe mais curta quando você deseja:  
- criar uma nova lista com base nos valores de uma lista existente (filtro) ou gerar uma nova lista aplicando alguma modificação
nos elementos de uma lista existente.

```
















