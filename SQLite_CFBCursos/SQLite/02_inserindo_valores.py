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


nome = str(input('Digite o nome: '))
telefone = str(input('Digite o telefone: '))
email = str(input('Digite o email: '))

comando_sql = "INSERT INTO contatos (nome, telefone, email) VALUES ('"+nome+"', '"+telefone+"', '"+email+"');"

vcon = conexao_banco()


def inserir_dados(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Valores inseridos')
    except Error as exx:
        print('Valores não inseridos:', str(exx).upper())


inserir_dados(vcon, comando_sql)

vcon.close()
