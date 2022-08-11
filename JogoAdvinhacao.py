import random
import os

erros=0
sorteado=random.randrange(0,100)
jogador = int(input('Digite seu numero: '))

while(sorteado!=jogador):
    os.system('cls')
    if (sorteado > jogador):
        print('Erro numero e maior')
    elif (sorteado < jogador):
        print('Erro numero e menor')
    erros+=1
    jogador=int(input('Digite seu numero: '))
print('Numero ',jogador ,'Voce acertou em ',(erros+1),'Tentativas')
        