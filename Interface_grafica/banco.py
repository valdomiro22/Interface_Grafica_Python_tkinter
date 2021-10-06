import sqlite3
from sqlite3 import Error
import os

pasta_app = os.path.dirname(__file__)  # Caminho dinamico
nome_banco = pasta_app + '/agenda.db'


def conexao_banco():
    con = None
    try:
        con = sqlite3.connect(nome_banco)
        print('Conectado')
    except Error as ex:
        print('Não conectou: ', ex)
    return con


def dql(query):  # select
    v_conexao = conexao_banco()
    c = v_conexao.cursor()
    c.execute(query)
    resultado = c.fetchall()
    comando_sql = "SELECT * FROM contatos;"
    print(c.fetchall())
    v_conexao.close()
    return resultado


def dml(query):  # insert, update, delete
    try:
        v_conexao = conexao_banco()
        c = v_conexao.cursor()
        c.execute(query)
        v_conexao.commit()
        v_conexao.close()
        print('Ação executada')
    except Error as ex:
        print('Ação não executada: ', ex)
