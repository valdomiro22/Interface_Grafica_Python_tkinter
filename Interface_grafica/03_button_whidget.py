from tkinter import *
import os

c = os.path.dirname(__file__)
nome_arquivo = c + '/nomes.txt'


def imprimir_dados():
    arquivo = open(nome_arquivo, 'a')
    arquivo.write('Nome.....: %s' % v_nome.get())
    arquivo.write('\nTelefone.: %s' % v_fone.get())
    arquivo.write('\nE-mail...: %s' % v_email.get())
    arquivo.write('\nOBS......: %s' % v_obs.get('1.0', END))
    arquivo.write('\n\n')
    arquivo.close()


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')
app.configure(background='#dde')

'''
anchor
N=Norte, S=Sul, E=Leste, W=Oeste
NE=Nordeste, SE=Sudeste, SO=Sudoeste, SW=Noroeste
'''
Label(app, text='Nome', background='#dde', foreground='#009', anchor=W).place(x=10, y=10, width=100, height=20)
v_nome = Entry(app)
v_nome.place(x=10, y=30, width=200, height=20)

Label(app, text='Telefone', background='#dde', foreground='#009', anchor=W).place(x=10, y=60, width=100, height=20)
v_fone = Entry(app)
v_fone.place(x=10, y=80, width=150, height=20)

Label(app, text='E-mail', background='#dde', foreground='#009', anchor=W).place(x=10, y=110, width=100, height=20)
v_email = Entry(app)
v_email.place(x=10, y=130, width=300, height=20)

Label(app, text='OBS:', background='#dde', foreground='#009', anchor=W).place(x=10, y=160, width=100, height=20)
v_obs = Text(app)
v_obs.place(x=10, y=180, width=300, height=80)

Button(app, text='Gravar', background='#48D1CC', command=imprimir_dados).place(x=10, y=270, width=70, height=20)


app.mainloop()
