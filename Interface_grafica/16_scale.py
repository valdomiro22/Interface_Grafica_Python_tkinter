from tkinter import *


def valor_scala():
    print(f'Valor do Scale: {str(sc_escala.get())}')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

lb_valor = Label(app, text='Valor')
lb_valor.pack()

sc_escala = Scale(app, from_=0, to=100, orient=HORIZONTAL)
sc_escala.set(30)  # Onde eu quero que o scale inicie
sc_escala.pack()


btn_valor = Button(app, text='Escala', command=valor_scala)
btn_valor.pack()

app.mainloop()
