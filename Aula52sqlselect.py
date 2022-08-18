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


# Consultar da Tabela

def consulta(conexao,sql):
    
    c=conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql="SELECT * FROM tb_contatos WHERE N_IDCONTATO=1"
res = consulta(vcon,vsql)

for r in res:
    print(r)

    
