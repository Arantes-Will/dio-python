# Em python tudo é um objeto, o que tornam funções objetos de primeira classe.
#Com isso podemos atribuir funções a variáveis, passá-las como parâmetro para funções, usá-las como valores em estrutura de dados, e usar como valor de retorno para uma função (closures)

def somar(a,b):
    return a+b

def exibir_resultado(a,b,funcao):
    resultado = funcao(a,b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

#Escopo local e escopo global
#Dentro da função: escopo é local e para usar objetos globais utilizamos a palavra chave global, que informa ao interpretador que a variável que está sendo manipulada no escopo local é global.(NÃO É UMA BOA PRÁTICA)