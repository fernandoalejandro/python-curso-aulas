import os
os.system('cls')


def somar(*num):
    r=0
    for n in num:
        r+=n

    print("Soma = ",r)

somar(5,2)
