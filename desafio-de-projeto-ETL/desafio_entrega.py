import pandas as pd

#Primeiramente fiz a parte de extração dos meus dados em um arquivo csv
teste = pd.read_csv("loja_cd.csv")

#Na parte de transformação, criei uma nova tabela informando o faturamento por cada cd vendido
teste_atualizado = teste.copy()
teste_atualizado['Faturamento'] = (teste_atualizado['Preço'] * teste_atualizado['Quantidade_Vendas']).round(2)

#Carregando os dados em um novo arquivo CSV
teste_atualizado.to_csv("loja_cd_atualizado.csv")


