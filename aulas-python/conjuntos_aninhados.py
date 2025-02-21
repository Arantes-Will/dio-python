contatos = {'guilherme@gmail.com': {'nome': 'guilherme', 'telefone': '3333-2221'},
'maria@hotmail.com': {'nome': 'maria', 'telefone': '5555-4444'},
'joao@outlook.com': {'nome': 'joao', 'telefone': '7777-6666'},
'ana@bol.com.br': {'nome': 'ana', 'telefone': '8888-7777'},
'pedro@gmail.com': {'nome': 'pedro', 'telefone': '9999-8888'}}

#telefone = (contatos['ana@bol.com.br']['telefone'])
#print(telefone)

#Iterar dicionários

#for chave in contatos:
    #print(chave, contatos[chave])

for chave,valor in contatos.items():
    print(chave,valor)

