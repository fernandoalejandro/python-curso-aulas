
tupla_carros=('hrv','golf','argo')
lista_carros=list(tupla_carros)
lista_carros[2]='bmw'
tupla_carros=tuple(lista_carros)

for x in tupla_carros:
    print(x)


