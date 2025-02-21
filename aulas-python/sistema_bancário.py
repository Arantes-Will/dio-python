#Criar um sistema bancário com as operações: sacar, depositar e vizualizar extrato
#O sistema deve permitir realizar 3 saques diários com limite máximo de R$500,00 por saque.
#Todos os saques devem ser armazenados em uma variável e exibidos a operação de extrato.

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor do deposito: '))
        if(valor < 0):
            print('\nValor inserido não válido, tente novamente.')
        else:
            saldo += valor
            extrato += f'DEPOSITO: R${valor:.2f} / VALOR ATUAL: R${saldo:.2f}.\n' 

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            if saldo == 0:
                print('\nVocê esta sem saldo!')
            else:
                saque = float(input('Informe o valor do saque: '))
                if(saque > saldo):
                    print('O valor solicitado excede o saldo disponível em sua conta.')
                else:
                    saldo -= saque
                    extrato += f'SAQUE: R${saque:.2f} / VALOR ATUAL: R${saldo:.2f}.\n'
                    numero_saques += 1
        else:
            print('\nO limite diário de saque foi atingido. Tente novamente amanhã.')

    elif opcao == 'e':
        print('\n****************** EXTRATO *******************')
        print(extrato)
        print('**********************************************\n')

    elif opcao == 'q':
        break
    
    else:
        print('\nOpção Inválida!')




