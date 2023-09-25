## 💻 Tuplas em Python


Tuplas são estruturas de dados muito parecidas com as listas, a diferença é que as tuplas são imutáveis.
```
frutas = ("laranja","pera","uva",)
letras = tuple ("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)
```

OBS: O processo de Estruturas aninhadas, fatiamento e iteração é a mesma de listas, a diferença é que como a tupla é imutável,
não conseguimos fazer modificações, ou seja, a tupla é usada quando temos certeza que não podemos modificar os elementos da tupla.

#### Métodos da classe tuple
```
cores = ("vermelho", "azul", "verde, "azul")
().count #Retorna a quantidade de elementos tem na tupla
cores.count("azul") #retorna 2
().index # Retorna a posição do elemento
cores.index("vermelho") #retorna 0
```



