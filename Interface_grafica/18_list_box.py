from tkinter import *


def imprimir_esporte():
    print(f'Esporte selecionado: {str(lb_esportes.get(ACTIVE))}')


def add_esporte():
    lb_esportes.insert(END, v_novo_esporte.get())


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

list_esportes = ['Futebol', 'Vôlei', 'Basquete']

lb_esportes = Listbox(app)

for esportes in list_esportes:
    lb_esportes.insert(END, esportes)


lb_esportes.pack()

btn_esporte = Button(app, text='Imprimir', command=imprimir_esporte)
btn_esporte.pack()

v_novo_esporte = Entry(app)
v_novo_esporte.pack()

inserir_esporte = Button(app, text='Adicionar', command=add_esporte)
inserir_esporte.pack()

app.mainloop()
