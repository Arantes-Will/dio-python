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

## Estruturas Condicionais e de Repetição

## Identação e blocos

Identar o código é uma forma de manter o código fonte mais legível e manutenível.
Mas em python o interpretador consegue determinar onde o bloco inicia e onde ele termina.
A identação em python é feita utilizando-se 4 espaços em branco
```
def sacar (self, valor: float) -> none:
    if self.saldo >= valor:
        self.saldo -= valor
```

## Estruturas condicionais
A estrutura condicional permite o desvio de fluxo de controle, quando determinadas expressões lógicas são atendidas.

#### if
```
saldo = 2000.0
saque = float (input ("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")

if saldo < saque:
    print("Saldo insuficiente!")
```
#### if/else
```
saldo = 2000.0
saque = float (input ("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando saque!")
else:
    print("Saldo insuficiente!")
```
#### if/elif/else
O elif é composto por uma nova expressão lógica, caso o bloco seja verdadeiro, será executado. Temos que tentar evitar criar grandes estruturas condicionais pois elas aumentam a complexidade do código.
```
opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato: "))

if opcao == 1:
    valor = float(input("Informe a quantia para o saque: "))
elif opcao == 2:
    print("Exibindo o extrato...")
else:
    sys.exit("Opção inválida")
```
#### if aninhado
```
if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")
```
#### if ternário
Permite escrever uma condição em uma única linha.
1º parte: retorno caso a expressão retorne verdadeiro
2º parte: expressão lógica
3º parte: retorno caso a expressão não seja atendida
```
status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")
```

        





































