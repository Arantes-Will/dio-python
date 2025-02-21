from datetime import datetime,timedelta

#criando data e hora
d = datetime(2023, 7, 19, 13, 45)
print(d)

#adicionando uma semana (O timedelta representa uma duração, a diferença entre duas datas ou horas)
d = d + timedelta(weeks = 1)
print(d)