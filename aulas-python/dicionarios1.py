#Um dicionário é um conjunto não-ordenado de pares chave: valor, onde as chaves são as unicas em uma dada instância do dicionário. 
#Dicionários podem armazenar qualquer tipo de objeto Python como valor, desde que a chave para esse valor seja um objeto imutável (strings e números)

#pessoa = {'nome': 'William','idade': 34}


pessoa = dict(nome = 'William', idade = 34)
print(pessoa)

pessoa['telefone'] = '129984-5871'
print(pessoa)

#Acesso aos dados

print(pessoa['nome']) #William




