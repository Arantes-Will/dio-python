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




