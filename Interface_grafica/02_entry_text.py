"""
Entry -> É um componente para linha limples
Text -> É um componente para multiplas linhas
"""


from tkinter import *

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

Label(app, text='E-Mail', background='#dde', foreground='#009', anchor=W).place(x=10, y=110, width=100, height=20)
v_email = Entry(app)
v_email.place(x=10, y=130, width=300, height=20)

Label(app, text='OBS:', background='#dde', foreground='#009', anchor=W).place(x=10, y=160, width=100, height=20)
v_obs = Text(app)  # Elemento de varias linhas
v_obs.place(x=10, y=180, width=300, height=80)


app.mainloop()
