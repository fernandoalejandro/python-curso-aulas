from distutils.util import execute
import sqlite3
from sqlite3 import Error
###### Criar Conexão
def ConexaoBanco():
    caminho="D:\\Downloads\\sqllite\\agenda.db"
    con=None

    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()


nome=input('Digite o nome: ')
telefone=input('Digite o telefone: ')
email=input('Digite o email: ')

vsql="INSERT INTO tb_contatos(T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO)VALUES('"+nome+"','"+telefone+"','"+email+"')"

# Inserir na Tabela
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro Inserido')
    except Error as ex:
        print(ex)

inserir(vcon,vsql)



