import os
import sqlite3
from sqlite3 import Error

#Conexão ao Banco de Dados
def ConexaoBanco():
    caminho="D:\\Downloads\\sqllite\\agenda.db"
    conecta = None
    try:
        conecta = sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return conecta

vcon=ConexaoBanco()


def query(conexao,sql):      #funcao que executa insert,update,delete
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Operacao Realizada com Sucesso')
        conexao.close()


def consultar(conexao,sql): #funcao para select
    c=conexao.cursor()
    c.execute(sql)
    res=c.fetchall()
    #conexao.close
    return res


def menuPrincipal():
    os.system('cls')
    print('1 - Inserir Novo Registro')
    print('2 - Deletar  Registro')
    print('3 - Atualizar Registro')
    print('4 - Consultar Registros')
    print('5 - Consultar Registro por nome Registro')
    print('6 - Sair')

def menuInserir():
    os.system('cls')
    vnome=input('Digite o nome: ')
    vtelefone=input('Digite o telefone: ')
    vemail=input('Digite o email: ')
    vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES ('"+vnome+"','"+vtelefone+"','"+vemail+"')"
    query(vcon,vsql)

def menuDeletar():
    os.system('cls')
    vid=input('Digite o ID do registro a ser deletado: ')
    vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+vid
    query(vcon,vsql)


def menuAtualizar():
    os.system('cls')
    vid=input('Digite o ID do registro a ser alterado: ')
    r=consultar(vcon,"SELECT * FROM tb_contatos WHERE N_IDCONTATO="+vid)
    rnome=r[0][1]
    rtelefone=r[0][2]
    remail=r[0][3]
    vnome=input('Digite o nome: ')
    vtelefone=input('Digite o telefone: ')
    vemail=input('Digite o email: ')
    if(len(vnome)==0): # se for igual, n foi digitado algo.
        vnome = rnome
    if(len(vtelefone)==0): # se for igual, n foi digitado algo.
        vtelefone = rtelefone
    if(len(vemail)==0):  # se for igual, n foi digitado
        vemail = remail
    vsql="UPDATE tb_contatos SET T_NOMECONTATO='"+vnome+"',T_TELEFONECONTATO='"+vtelefone+"',T_EMAILCONTATO='"+vemail+"' WHERE N_IDCONTATO="+vid
    query(vcon,vsql)


def menuConsultar():
    vsql="SELECT * FROM tb_contatos"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:<3} Nome:{1:<30} Telefone:{2:<14} Email:{3:<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
            os.system('pause')
            os.system('cls')
    print('Fim da lista')
    os.system('pause')
    



def menuConsultarNomes():
    vnome=input('Digite o nome : ')
    vsql="SELECT * FROM tb_contatos WHERE T_NOMECONTATO LIKE '%"+vnome+"%'"
    res=consultar(vcon,vsql)
    vlim=10
    vcont=0
    for r in res:
        print("ID:{0:<3} Nome:{1:<30} Telefone:{2:<14} Email:{3:<30}".format(r[0],r[1],r[2],r[3]))
        vcont+=1
        if(vcont>=vlim):
            vcont=0
            os.system('pause')
            os.system('cls')
    print('Fim da lista')
    os.system('pause')






opcao = 0
while opcao !=6:
    menuPrincipal()
    opcao=int(input('Digite uma Opcao entre 1 ate 6 : '))
    if opcao==1:
        menuInserir()
    elif opcao==2:
        menuDeletar()
    elif opcao==3:
        menuAtualizar()
    elif opcao==4:
        menuConsultar()
    elif opcao==5:
        menuConsultarNomes()
    elif opcao==6:
        os.system('cls')
        print('Programa Finalizado')
    else:
        os.system('cls')
        print('opcao invalida')
        os.system('pause')
vcon.close()
os.system('pause')      #Parte1




