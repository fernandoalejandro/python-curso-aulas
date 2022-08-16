import datetime

data=datetime.datetime.now()
nasc=datetime.datetime(1993,4,29)

print(data.day,'/',data.month,'/',data.year)
print(nasc.strftime('%A'))

#%a
#%A texto dia da semana
#%w num dia da semana
#%d num dia do mês
#%b texto mes abreviado
#%B texto mes
#%m num do mês
#%y Ano com dois digitos
#%Y ano com quatro digitos
#%H 00 - 23
#%I 00 - 12
#%p AM/ PM
#%M minutos
#%S segundos
#%f microsegundos
#%j Dia do ano 365
#%W Numero da semana do ano
