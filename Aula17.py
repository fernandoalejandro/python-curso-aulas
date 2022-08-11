import os
os.system('cls')
    #Chave/Key - Valor / Value
carro={'Fabricante':'Honda',
'Modelo':'HRV',
'Ano':'2016',
'Cor':'Prata'
}  #dictionari

carro['Cambio']='Automatico' # Adiciona uma chave com valor.

carro['Cor']='Preto'  #mudando a o valor da chave para preto

print('tamanho do dictionary : ',len(carro)) # tamanho do dictonari
for c,v in carro.items():
    print('Valor da Chave:',c,'Valor do Valor: ',v)
    