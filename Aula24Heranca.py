class NPC: #Pai, Base, Super
    def __init__(self,nome,time,forca,municao):
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print('Nome: ',self.nome)
        print('Time: ',self.time)
        print('forca: ',self.forca)
        print('Municao: ',self.municao)
        print('Vivo: ',('sim' if self.vivo else 'nao'))
        print('Energia: ',self.energia)
        print('...................................')


class Soldado(NPC):   #Classe Filho
    def __init__(self, nome, time):
            self.forca=200
            self.municao=200
            super().__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self, nome, time):
        self.forca=100
        self.municao=20
        super().__init__(nome, time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self, nome, time):
        self.forca=400
        self.municao=500
        super().__init__(nome, time, self.forca, self.municao)
    def inf(self):  #chama func info do pai
            super().info()


s1=Guarda("BEAVIS",1)      #CHAMADA DA INSTANCIA
s2=Soldado("AKKRIOS",1)
s3=Elite("CEFALEXINA",1)
s4=Guarda("OhNoEZ",2)
s5=Soldado('TuaTia',2)
s6=Elite('Talbot',2)

s1.info()
s2.info()
s3.info()
s4.info()
s5.info()
s6.inf()



        


