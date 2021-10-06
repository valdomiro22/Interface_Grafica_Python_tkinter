from tkinter import *


def imprimir_senha():
    print(f'Senha digitada: {v_senha.get()}')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_senha = StringVar()

p_senha = Entry(app, textvariable=v_senha, show='@')
p_senha.pack()

btn_mostra_senha = Button(app, text='Imprimir senha', command=imprimir_senha)
btn_mostra_senha.pack()

app.mainloop()
