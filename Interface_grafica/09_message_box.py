from tkinter import *
from tkinter import messagebox


def mostrar_msg(tipo_msg, msg):
    if tipo_msg == '1':
        messagebox.showinfo(title='CFB Cursos', message=msg)
    elif tipo_msg == '2':
        messagebox.showwarning(title='CFB Cursos', message=msg)
    elif tipo_msg == '3':
        messagebox.showerror(title='CFB Cursos', message=msg)


v_msg = 'Curso de Python com Tkinter'

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

v_num_cxtexto = StringVar()

Label(app, text='Tipo de caixa 1, 2 ou 3:').pack()
tb_num = Entry(app, textvariable=v_num_cxtexto)
v_num_cxtexto.set('1')
tb_num.pack()

btn_msg = Button(app, text='Mostrar mensagem', command=lambda: mostrar_msg(v_num_cxtexto.get(), v_msg))
btn_msg.pack()

app.mainloop()
