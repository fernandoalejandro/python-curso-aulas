import os
os.system('cls') #limpa tela


carros = []
carro = input('Digite o nome do novo carro: ')

while carro != '-1': # '!=' diferente
    carros.append(carro)
    carro = input('Digite o nome do novo carro: ')


for x in carros:
    print(x)
print('\nFim do loop')