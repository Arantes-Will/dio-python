
def exibir_mensagem(nome):
    print(f"Olá, seja bem vindo {nome}!")

exibir_mensagem("William")

#Retornando Valores
#Toda função Python retorna None por padrão e em Python uma função pode retornar mais de um valor

def calcular_total(numeros):
    return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
    antecessor = numero-1
    sucessor = numero+1

    return antecessor, sucessor

#print(calcular_total([10,20,34]))
#print(retorna_antecessor_e_sucessor(10)) #retorna uma tupla

#Argumentos nomeados (posso passar chave e valor)

def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #Passando os valores
#Garante que não haverá erro ao passar os argumentos
salvar_carro(marca = "Fiat",modelo = "Palio",ano = 1999, placa = "ABC-1234")



