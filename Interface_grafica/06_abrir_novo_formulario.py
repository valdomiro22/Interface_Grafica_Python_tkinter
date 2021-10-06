from tkinter import *
import os


pasta_app = os.path.dirname(__file__)


def sem_comando():
    print('')


def novo_contato():
    # exec(open(pasta_app + '/04_gravando_em_banco_de_dados.py').read(), {'x': 10})  x é um parametro que sera passado
    exec(open(pasta_app + '/04_gravando_em_banco_de_dados.py').read(), {'x': 10})


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')

barra_menus = Menu(app)
menu_contatos = Menu(barra_menus, tearoff=0)
menu_contatos.add_command(label='Novo', command=novo_contato)
menu_contatos.add_command(label='Pesquisar', command=sem_comando)
menu_contatos.add_command(label='Deletar', command=sem_comando)
menu_contatos.add_separator()
menu_contatos.add_command(label='Fechar', command=app.quit)
barra_menus.add_cascade(label='Contatos', menu=menu_contatos)

menu_manutencao = Menu(barra_menus, tearoff=0)
menu_manutencao.add_command(label='Bando de Dados', command=sem_comando)
barra_menus.add_cascade(label='Manutanção', menu=menu_manutencao)

menu_sobre = Menu(barra_menus, tearoff=0)
menu_sobre.add_command(label='CFB Cursos', command=sem_comando)
barra_menus.add_cascade(label='Sobre', menu=menu_sobre)

app.config(menu=barra_menus)

app.mainloop()
