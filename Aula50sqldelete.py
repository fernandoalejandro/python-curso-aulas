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


# Deletar da Tabela

def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro Deletado')
    except Error as ex:
        print(ex)
    finally:
        print('Registro Removido')
vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO=4"

deletar(vcon,vsql)