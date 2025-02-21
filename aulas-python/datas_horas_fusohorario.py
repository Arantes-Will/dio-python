#módulo datetime (responsável pela manipulação de data e hora)
from datetime import date, datetime, time
#import datetime  neste caso na hora de chamar o date, precisaria colocar d = datetime.date(2025, 2, 20)

data = date(2025, 2, 20) #(year, month, day) 1< year < 9999
print(data)

#Data local atual
print(date.today())

#datetime (year, month, day, hour = 0, minute = 0, second = 0, microsecond = 0, tzinfo=None, *, fold = 0)
data_hora = datetime(2023, 7, 10)
print(data_hora)
print(datetime.today())

#Horas
hora = time(10, 20, 0)
print(hora)
