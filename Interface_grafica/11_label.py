from tkinter import *
from tkinter import messagebox


def mostrar_msg():
    messagebox.showinfo(title='CFB Cursos', message='CFB Cursos, Curso de Python com Tkinter')


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_num_cxtexto = StringVar()

fr_quadro1 = Frame(app, borderwidth=1, relief='solid')
# relief - flat, raised, sunken, solid
fr_quadro1.place(x=10, y=10, width=300, height=100)

lb_tipo = Label(fr_quadro1, text='Tipo de caixa 1, 2 ou 3:')
lb_tipo.place(x=12, y=10)
tb_num = Entry(fr_quadro1, textvariable=v_num_cxtexto)
v_num_cxtexto.set('1')
tb_num.place(x=12, y=30, width=100)

btn_msg = Button(fr_quadro1, text='Mostrar mensagem', command=lambda: mostrar_msg)
btn_msg.place(x=12, y=60)

fr_quadro2 = Frame(app, borderwidth=1, relief='solid', background='#008')
# relief - flat, raised, sunken, solid
fr_quadro2.place(x=10, y=120, width=300, height=100)

lb_canal = Label(fr_quadro2, text='CFB Cursos', backgroun='#008', foreground='#fff', font=('Arial', 25))
lb_canal.pack(side=LEFT, fill=X, expand=True)

app.mainloop()
