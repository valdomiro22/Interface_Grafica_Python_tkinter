from tkinter import *
from tkinter import messagebox


def futebol_clicado():
    print(f'Futebol: {v_futebol.get()}')


def volei_clicado():
    print(f'Volei: {v_volei.get()}')


def basquete_clicado():
    print(f'Basquete: {v_basquete.get()}')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_futebol = IntVar()
v_volei = IntVar()
v_basquete = IntVar()

fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
# relief - flat, raised, sunken, solid
fr_quadro1.place(x=10, y=10, width=300, height=100)

cb_futebol = Checkbutton(fr_quadro1, text='Futebol', variable=v_futebol,
                         onvalue=1, offvalue=0, command=futebol_clicado)
cb_futebol.pack(side=LEFT)

cb_volei = Checkbutton(fr_quadro1, text='Volei', variable=v_volei,
                       onvalue=1, offvalue=0, command=volei_clicado)
cb_volei.pack(side=LEFT)

cb_basquete = Checkbutton(fr_quadro1, text='Basquete', variable=v_basquete,
                          onvalue=1, offvalue=0, command=basquete_clicado)
cb_basquete.pack(side=LEFT)

app.mainloop()
