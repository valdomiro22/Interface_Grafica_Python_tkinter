from tkinter import *
from tkinter import ttk


def mostrar():
    print(f'Esporte selecionado: {cb_esportes.get()}')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

list_esportes = ['Futebol', 'Volei', 'Basquete']

lb_esportes = Label(app, text='Esportes')
lb_esportes.pack()

cb_esportes = ttk.Combobox(app, values=list_esportes)
cb_esportes.set('Futebos')
cb_esportes.pack()


btn_esporte = Button(app, text='Esporte Selecionado', command=mostrar)
btn_esporte.pack()


app.mainloop()
