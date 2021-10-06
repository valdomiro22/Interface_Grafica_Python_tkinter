from tkinter import *


def imprimir_esporte():
    ve = v_esportes.get()

    if ve == 'f':
        print('Futebol Selecionado')
    elif ve == 'v':
        print('Volei Selecionado')
    elif ve == 'b':
        print('Basquete Selecionado')
    else:
        print('Nenhum esporte selecionado')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_esportes = StringVar()
v_cor = StringVar()

bl_esportes = Label(app, text='Esportes')
bl_esportes.pack()

rb_futebol = Radiobutton(app, text='Futebol', value='f', variable=v_esportes)
rb_futebol.pack()

rb_volei = Radiobutton(app, text='Volei', value='v', variable=v_esportes)
rb_volei.pack()

rb_basquete = Radiobutton(app, text='Basquete', value='b', variable=v_esportes)
rb_basquete.pack()

rb_cor = Radiobutton(app, text='Verde', value='#0f0', variable=v_cor)
rb_cor.pack()

rb_cor = Radiobutton(app, text='Vermelho', value='#f00', variable=v_cor)
rb_cor.pack()

brn_esporte = Button(app, text='Esporte selecionado', command=imprimir_esporte)
brn_esporte.pack()


app.mainloop()
