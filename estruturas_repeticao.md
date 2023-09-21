## 💻 Estruturas de Repetição

### O que são estruturas de repetição
São estruturas utilizadas para repetir um trecho de código um determinado número de vezes. 
Esse número pode ser conhecido previamente ou determinado através de uma expressão lógica.

#### Comando for
É usado para percorrer um objeto iterável. Faz sentido usar o for quando 
sabemos o número exato de vezes que nosso bloco de código deve ser executado,
ou quando queremos percorrer um objeto iterável.

```
texto = input("Informe o texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()
```
#### Função Range
É uma função built-in do Python, ela é usada para produzir uma sequência de
números inteiros a partir de um ínicio(inclusivo) para um fim (exclusivo).
Se usarmos range(i,j) será produzido:
i, i+1, i+2, i+3, ... , j-1.
Argumentos: stop(obrigatório), start(opcional) e step (opcional)
```
list(range(4))
````

#### Comando while
O comando while é usado para repetir um bloco de código várias vezes. Faz
sentido usar while quando não sabemos o número exato de vezes que nosso 
bloco de código deve ser executado.

```
opcao = 1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
    
```

