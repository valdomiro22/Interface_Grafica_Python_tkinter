from tkinter import *


def imprimir_esporte():
    ve = v_esportes.get()

    if ve == 'Futebol':
        print('Futebol Selecionado')
    elif ve == 'Volei':
        print('Volei Selecionado')
    elif ve == 'Basquete':
        print('Basquete Selecionado')
    else:
        print('Nenhum esporte selecionado')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

lista_esportes = ['Futebol', 'Volei', 'Basquete']

v_esportes = StringVar()
v_esportes.set(lista_esportes[0])

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

op_esportes = OptionMenu(app, v_esportes, *lista_esportes)
op_esportes.pack()


brn_esporte = Button(app, text='Esporte selecionado', command=imprimir_esporte)
brn_esporte.pack()


app.mainloop()
