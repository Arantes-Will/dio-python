# DIO | Resumos Python
## 💻 Conhecendo a linguagem de programação Python

| Tipos:   | Os tipos built-in são: |
|----------|---------------------|
| Texto    | str                 |
| Numérico | int, float, complex |
| Sequência| list, tuple, range  |
| Mapa | dict |
| Coleção | set, frozenset |
| Booleano | bool |
| Binário | bytes, bytearray, memoryview |

#### Numérico:  
Números inteiros : int  
Números de ponto flutuante: float 

#### Booleano:
True ou False 

#### String
Usadas para representar valores alfanúmericos
str

## Variáveis e Constantes

#### Variáveis
```
age = 32
name = "William Arantes"
print( f' Meu nome e {name} e eu tenho {age} ano(s) de idade.')
```
OBS: Em python não precisamos definir o tipo de dados da variável, isto é feita de forma automática. 

#### Constantes
São utilizadas para armazenar valores porém o valor é imutável! 
Para fazer isto devemos criar uma variável toda em letras maiúsculas.

```
ABS_PATH = 'home/..../..../.....'
DEBUG = True
STATES = [SP,RJ,MG]
```
OBS: Como boas praticas utilizar snake case, e escolher nomes sugestivos. Exemplo: calcula_valor, saldo_final ...

## Convertendo Tipos
Exemplo:
```
#Aqui fizemos uma conversão de float para int como exemplo
preco = 10.0
preco = int(preco)
print(preco)
#Aqui fizemos uma conversão de string para float como exemplo
numero = "18.9"
print(float(numero))
```
## Funções de Entrada e Saída

#### Lendo valores com a função input  
A função built-in input é utilizada quando queremos ler dados de entrada padrão, a função lê a entrada, converte para string
e retorna o valor.

## Tipo de Operadores com Python

#### Operadores Aritméticos

Os operadores aritiméticos executam operações matemáticas

| Tipo:   | Operador |
|----------|---------------------|
| Adição   | +                 |
| Subtração | - |
| Multiplicação| *  |
| Divisão | / |
| Divisão Inteira| // |
| Módulo | % (Resto da Divisão) |
| Exponenciação | ** |

#### Operadores de Comparação

São operadores utilizados para comparar dois valores.

| Tipo:   | Operador |
|----------|---------------------|
| Igualdade   | ==                |
| Diferença | != |
| Maior que | >  |
| Maior ou igual | >= |
| Menor que| < |
| Menor ou igual | <= |

#### Operadores de atribução

São operadores utilizados para definir o valor inicial ou sobrescrever o valor de uma variável

| Tipo:   | Operação |
|----------|---------------------|
| Atribuição   | saldo = 500           |
| Atribuição com adição | saldo += 200 |
| Atribuição com subtração | saldo -= 200 |
| Atribuição com multiplicação | saldo *= 200 |
| Atribuição com divisão | saldo /= 200 |
| Atribuição com divisão inteira| saldo //= 200 |
| Atribuição com modulo | saldo %= 200 |
| Atribuição com exponeciação | saldo **= 200 |

#### Operadores Lógicos

São operadores utilizados em conjunto com os operadores de comparação, para montar uma expressão lógica.

| Tipo:   | Operação |
|----------|---------------------|
| Operador E (and)   | Verdadeiro quando os dois valores forem verdadeiros|
| Operador OU (or) | Falso quando os dois valores forem falsos |
| Operador NEGAÇÃO (not) | Inverso 

#### Operadores de identidade

Comparam se possuem o mesmo endereço de memória
```
is
```
#### Operadores de associação

São operadores utilizados para verificar se um objeto está presente em uma sequência.
```
in
```
































