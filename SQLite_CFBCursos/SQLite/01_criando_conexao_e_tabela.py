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


comando_sql = """CREATE TABLE contatos (id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(30),
            telefone VARCHAR(14),
            email VARCHAR(30)
            );
        """
vcon = conexao_banco()


def criar_tabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print('Tabela criada')
    except Error as exx:
        print('Tabela não criada:', str(exx).upper())


criar_tabela(vcon, comando_sql)

vcon.close()
