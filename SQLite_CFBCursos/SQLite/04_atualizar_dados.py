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


comando_sql = "UPDATE contatos SET email = 'antonia958@yahoo.com' WHERE nome = 'antonia';"

vcon = conexao_banco()


def consultar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Dados alterados')
    except Error as exx:
        print('Dados não alterados:', str(exx).upper())


consultar(vcon, comando_sql)

vcon.close()
