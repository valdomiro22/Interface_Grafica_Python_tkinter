import os
import sqlite3
from sqlite3 import Error


def conexao_bando():
    caminho = '/home/valdomiro/Documentos/Paython/cfbCursos/SQLite_CFBCursos/Agenda_SQLite/agenda.db'
    conect = None
    try:
        conect = sqlite3.connect(caminho)
        print('Conexão bem sucedida')
    except Error as ex:
        print('Não foi possivel se conectar: ', ex)
    return conect


conectar = conexao_bando()


def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Comando executado')
    except Error as ex:
        print(f'Erro ao executar o comando: {ex}')
    finally:
        print('Operação realizada com sucesso')


def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado


def menu_principa():
    print('[1] - Inserir novo registro')
    print('[2] - Deletar Reristro')
    print('[3] - Atualizar Registro')
    print('[4] - Consultar Registros')
    print('[5] - Consultar Registro por Nome')
    print('[6] - Sair')


def inserir():
    # os.system('clear')
    v_nome = input('Digite o nome: ')
    v_telefone = input('Digite o telefone: ')
    v_email = input('Digite o email: ')

    v_sql = f"""INSERT INTO contatos (nome, telefone, email) 
                VALUES ('{v_nome}', '{v_telefone}', '{v_email}');
            """

    query(conectar, v_sql)


def deletar():
    v_id = input('Digite o ID do registro a ser deletado: ')

    vsql = f"""DELETE FROM contatos WHERE id =  {v_id};"""
    query(conectar, vsql)


def atualizar():
    v_id = input('Digite o ID do registro a ser alterado: ')
    r = consultar(conectar, f"""SELECT * FROM contatos WHERE id = '{v_id}';""")
    r_nome = r[0][1]
    r_telefone = r[0][2]
    r_email = r[0][3]
    v_nome = input('Digite o nome: ')
    v_telefone = input('Digite o telefone: ')
    v_email = input('Digite o email: ')

    if len(v_nome) == 0:
        v_nome = r_nome
    if len(v_telefone) == 0:
        v_telefone = r_telefone
    if len(v_email) == 0:
        v_email = r_email

    vsql = f"""UPDATE contatos SET nome = '{v_nome}', telefone = '{v_telefone}', email = '{v_email}' WHERE id = {v_id};
            """
    try:
        query(conectar, vsql)
        print('Alterações feitas')
    except Error as ex:
        print('Alterações não feitas: ', ex)


def menu_consultar():
    vsql = """SELECT * FROM contatos"""
    res = consultar(conectar, vsql)
    v_limite = 10
    v_cont = 0
    print()
    for r in res:
        print("ID: {0: <3}  Nome:{1: <15} Telefone:{2: <15} E-mail:{3: <15}".format(r[0], r[1], r[2], r[3]))
        v_cont += 1

        if v_cont >= v_limite:
            v_cont = 0
    print()


def consultar_nome():
    v_nome = input('Digite o nome: ')
    vsql = f"""SELECT * FROM contatos WHERE nome LIKE '%{v_nome}%'"""
    res = consultar(conectar, vsql)
    v_limite = 10
    v_cont = 0
    print()
    for r in res:
        print("ID:{0: <3}  Nome:{1: <15} Telefone:{2: <15} E-mail:{3: <15}".format(r[0], r[1], r[2], r[3]))
        v_cont += 1

        if v_cont >= v_limite:
            v_cont = 0
    print()


opc = 0
while opc != 6:
    menu_principa()
    opc = int(input('Escolha uma das opções: '))

    if opc == 1:
        inserir()
    elif opc == 2:
        deletar()
    elif opc == 3:
        atualizar()
    elif opc == 4:
        menu_consultar()
    elif opc == 5:
        consultar_nome()
    elif opc == 6:
        print('Programa finalizado')
    else:
        print('Opção invalida')

conectar.close()
