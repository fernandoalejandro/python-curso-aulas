import os



carros=[]

class Carro:
    nome=''
    potencia=0
    velMaxima=0
    ligado=False
    def __init__(self,nome,potencia):   #Construtor
        self.nome=nome
        self.potencia=potencia
        self.velMaxima=int(potencia)*2
        self.ligado=False
    def ligar(self):   #Metodo
        self.ligado=True
    def desligar(self):    #Metodo
        self.ligado=False

    def info(self):   #Metodo
        print('Nome',self.nome)
        print('Potencia: ',self.potencia)
        print('Velocidade Maxima: ',self.velMaxima)
        print('Ligado :','sim' if self.ligado==True else 'nao')

def menu():    #Funcao para criar o Menu
    os.system('cls') or None
    print('1 - Novo Carro')
    print('2 - Informacoes do Carro')
    print('3 - Excluir Carro')
    print('4 - Desligar Carro')
    print('5 - Listar Carros')
    print('6 - Sair')
    print('7 - Quantidade de Carros',len(carros))
    opcao=input("Digite uma opcao: ")
    return opcao

def NovoCarro():  #Funcao para criar o Carro
    os.system('cls') or None
    n=input('Nome do Carro: ')
    p=input('Potencia do Carro: ')
    car = Carro(n,p)
    carros.append(car)
    print('Novo Carro criado')
    os.system('pause')

def informacoes(): #Funcao para saber se o carro existe na lista
    os.system('cls') or None
    n=input('Informe o numero do carro que deseja ver as informacoes: ')
    try:
        carros[int(n).info()]
    except:
            print('Carro nao existe na lista')
            os.system('pause')
def excluirCarro():
    os.system('cls') or None
    n=input('Informe o numero do carro que deseja excluir: ')
    try:
        del carros[int(n)]
    except:
        print('Carro nao existe na lista')
        os.system('pause')


def ligarCarro(): #Funcao para ligar o carro
    os.system('cls') or None
    n=input('Informe o numero do carro que deseja ligar: ')
    try:
        carros[int(n)].ligar()
        print('Carro ligado')
    except:
        print('Carro nao existe na lista')
        os.system('pause')


def desligarCarro(): #Funcao para desligar o carro
    os.system('cls') or None
    n=input('Informe o numero do carro que deseja desligar: ')
    try:
        carros[int(n)].desligar()
        print('Carro desligado')
    except:
        print('Carro nao existe na lista')
        os.system('pause')


def listarCarros(): #Funcao para listar o carro
    os.system('cls') or None
    p=0
    for c in carros:
        print(p,' - ',c.nome)
        p=p+1
    os.system('pause')

ret=menu()
while ret < '7':
    if ret=='1':
        NovoCarro()
    elif ret=='2':
        informacoes()
    elif ret=='3':
        excluirCarro()
    elif ret=='4':
        ligarCarro()
    elif ret=='5':
        desligarCarro()
    elif ret=='6':
        listarCarros()
    ret=menu()
os.system('cls') or None
print('Programa Finalizado')






    

