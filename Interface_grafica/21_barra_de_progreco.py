from tkinter import *
from tkinter import ttk


def valor_barra(m):
    cont = 0
    etapas = m / 100

    while cont < etapas:
        cont = cont + 1
        i = 0

        while i < 10000:
            i = i + 1
            v_barra.set(cont)
            app.update()


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_barra = DoubleVar()
v_barra.set(0)

pb = ttk.Progressbar(app, variable=v_barra, maximum=100)
pb.place(x=0, y=0, width=500, height=40)

btn = Button(app, text='Definir Barra', command=lambda: valor_barra(10000))
btn.place(x=0, y=50, width=100, height=40)

app.mainloop()
