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


# Atualizar da Tabela

def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print('Registro atualizado')
vsql="UPDATE tb_contatos SET T_NOMECONTATO='Bruno', T_TELEFONECONTATO='(11)99999-9999', T_EMAILCONTATO='bruno@email.com.br' WHERE N_IDCONTATO=1"
atualizar(vcon,vsql)


