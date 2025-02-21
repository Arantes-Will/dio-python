#Quando trabalhamos com data e hora, lidar com fusos horáios é uma necessidade comum. Python facilita isso através do módulo 'pytz'
import pytz
from datetime import datetime, timezone, timedelta

data = datetime.now(pytz.timezone('Europe/Oslo'))
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
print(data)
print(data2)

#Trabalhando com tz sem bibliotecas externas
#O Python permite fazer isso com o módulo datetime padrão, embora seja um pouco mais complexo do que usando bibliotecas como 'pytz'

data_oslo = datetime.now(timezone(timedelta(hours=2)))
data_sp = datetime.now(timezone(timedelta(hours=-3)))
print(data_oslo)
print(data_sp)