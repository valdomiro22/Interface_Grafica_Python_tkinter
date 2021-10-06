import sqlite3
from sqlite3 import Error


def conexao_banco():
    caminho = '/home/valdomiro/Documentos/Paython/cfbCursos/SQLite_CFBCursos/agenda.db'
    con = None
    try:
        con = sqlite3.connect(caminho)
        print('Conexao bem sucedida')
    except Error as ex:
        print('Conexão não deu certo: ', str(ex).upper())
    return con


comando_sql = "SELECT * FROM contatos;"

vcon = conexao_banco()


def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print(c.fetchall())
    except Error as exx:
        print('Não foi possível consultar:', str(exx).upper())


consultar(vcon, comando_sql)

vcon.close()
