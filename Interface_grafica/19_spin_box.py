from tkinter import *


def imprimir_valor():
    print(f'Valor Selecionado: {sb_valores.get()}')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

# sb_valores = Spinbox(app, from_=0, to=100)
sb_valores = Spinbox(app, values=(1, 23, 3, 4, 5))
sb_valores.pack()

btn_valor = Button(app, text='Imprimir', command=imprimir_valor)
btn_valor.pack()

app.mainloop()
