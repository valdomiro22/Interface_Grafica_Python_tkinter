from tkinter import *
import os
import banco

# c = os.path.dirname(__file__)
# nome_arquivo = c + '/nomes.txt'

# print(x)


def imprimir_dados():
    if tb_nome.get() != '':
        v_nome = tb_nome.get()
        v_telefone = tb_fone.get()
        v_email = tb_email.get()
        v_obs = tb_obs.get('1.0', END)

        v_query = f"""
                    INSERT INTO contatos (nome, telefone, email, obs) 
                    VALUES ('{v_nome}', '{v_telefone}', '{v_email}', '{v_obs}');
                  """

        banco.dml(v_query)

        tb_nome.delete(0, END)
        tb_fone.delete(0, END)
        tb_email.delete(0, END)
        tb_obs.delete('1.0', END)

        print('Dados gravados')
    else:
        print('Erro')


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
tb_nome = Entry(app)
tb_nome.place(x=10, y=30, width=200, height=20)

Label(app, text='Telefone', background='#dde', foreground='#009', anchor=W).place(x=10, y=60, width=100, height=20)
tb_fone = Entry(app)
tb_fone.place(x=10, y=80, width=150, height=20)

Label(app, text='E-mail', background='#dde', foreground='#009', anchor=W).place(x=10, y=110, width=100, height=20)
tb_email = Entry(app)
tb_email.place(x=10, y=130, width=300, height=20)

Label(app, text='OBS:', background='#dde', foreground='#009', anchor=W).place(x=10, y=160, width=100, height=20)
tb_obs = Text(app)
tb_obs.place(x=10, y=180, width=300, height=80)

Button(app, text='Gravar', background='#48D1CC', command=imprimir_dados).place(x=10, y=270, width=70, height=20)


app.mainloop()
