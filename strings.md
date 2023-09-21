## 💻 Manipulando Strings com Python


#### Conhecendo métodos úteis da classe string
##### Maiúscula, minúscula e título
```
curso = "pYtHon"
print(curso.upper())
print(curso.lower())
print(curso.title())
```
##### Eliminando espaços em branco
```
print(curso.strip())
print(curso.lstrip())
print(curso.rstrip())
```
##### Junções e centralização
```
print(curso.center(10, "#"))
print(".".join(curso))
```
#### Interpolação de variáveis
Em python temos 3 formas de interpolar variáveis em strings  
1º Usando o sinal % (não é atualmente recomendada)  
2º Metodo format  
3º f strings  

```
#Método format
nome = "Will"
idade = 32
profissao = "programador"
linguagem = "Python"

print("Olá, ,e chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado no curso de {}.".format(nome, idade, profissao, linguagem))
#Com a posição
print("Olá, ,e chamo {3}. Eu tenho {2} anos de idade, trabalho como {1} e estou matriculado no curso de {0}.".format(linguagem, profissao, idade, nome))
```

```
#Método f-string
nome = "Will"
idade = 32
profissao = "programador"
linguagem = "Python"

print(f"Olá, ,eu chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado no curso de {linguagem}.")
```

#### Fatiamento de strings
É uma técnica utilizada para retornar substrings (parte da string original), informando inicio (start), fim (stop) e passo (step):  
[start: stop[,step]].

#### Strings de multiplas linhas  
Informando 3 aspas simples ou duplas durante a atribuição. Elas podem ocupar várias linhas do código, e todos os espaços em branco são incluídos na string final.

```
nome = "William"

print(f"""Olá meu nome é {nome}, 
eu estou estudando Python.
Esta mensagem tem diferentes recuos""")
```











