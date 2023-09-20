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














