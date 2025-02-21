from datetime import timedelta,datetime

tipo_carro = 'M' #P, M, G
tempo_pequeno = 30
tempo_medio = 3000
tempo_grande = 60
data_atual = datetime.now() #(today) / utcnow


if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes = tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto as {data_estimada}')    
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes = tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto as {data_estimada}')  
else:
    data_estimada = data_atual + timedelta(minutes = tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto as {data_estimada}')  
