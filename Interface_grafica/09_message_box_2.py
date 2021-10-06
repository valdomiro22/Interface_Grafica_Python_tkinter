from tkinter import *
from tkinter import messagebox


def mostrar_msg(tipo_msg, msg):
    if tipo_msg == '1':
        messagebox.showinfo(title='CFB Cursos', message=msg)
    elif tipo_msg == '2':
        messagebox.showwarning(title='CFB Cursos', message=msg)
    elif tipo_msg == '3':
        messagebox.showerror(title='CFB Cursos', message=msg)


def resetar_tb():
    resultado = messagebox.askyesno('Resetar', 'Confirma reset textbox?')
    # askyesno / askquestion - TRUE and FALSE
    # askokcancel - OK e CANCELAR
    # askretrycancel - REPETIR E CANCELAR
    # askyesnocancel - YES, NO and CANCELAR

    if resultado:
        tb_num.delete(0, END)
        tb_num.insert(0, '1')


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

btn_reset = Button(app, text='Resetar TextBox', command=resetar_tb)
btn_reset.pack()

app.mainloop()
