from datetime import datetime

#Utilizando o strftime
data_hora_atual = datetime.now()
data_hora_str = '2025-02-21 10:12'
mascara_ptbr = '%d/%m/%y %a' #Olhar a documentação,
mascara_en = '%Y-%m-%d %H:%M'

print(data_hora_atual.strftime(mascara_ptbr))


#Utilizando o strptime
print(datetime.strptime(data_hora_str, mascara_en ))
