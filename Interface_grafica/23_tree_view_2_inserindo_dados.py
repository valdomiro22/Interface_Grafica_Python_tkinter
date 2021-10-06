from tkinter import *
from tkinter import ttk
from tkinter import messagebox


def inserir():
    if v_id.get() == '' or v_nome.get() == '' or v_telefone.get() == '':
        messagebox.showinfo(title='ERRO', message='Digite todos os dados')
        return
    tv.insert('', 'end', values=(v_id.get(), v_nome.get(), v_telefone.get()))

    v_id.delete(0, END)
    v_nome.delete(0, END)
    v_telefone.delete(0, END)
    v_id.focus()


def deletar():
    print()


def obter():
    print()


app = Tk()
app.title('CFB Cursos')
app.geometry('550x350')

lb_id = Label(app, text='ID')  # , anchor=W
v_id = Entry(app)

lb_nome = Label(app, text='NOME')  # , anchor=W
v_nome = Entry(app)

lb_telefone = Label(app, text='TELEFONE')  # , anchor=W
v_telefone = Entry(app)

tv = ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')

btn_inserir = Button(app, text='Inserir', command=inserir)
btn_deletar = Button(app, text='Deletar', command=deletar)
btn_obter = Button(app, text='Obter', command=obter)

lb_id.grid(column=0, row=0, stick='w')
v_id.grid(column=0, row=1)

lb_nome.grid(column=1, row=0, stick='w')
v_nome.grid(column=1, row=1)

lb_telefone.grid(column=2, row=0, stick='w')
v_telefone.grid(column=2, row=1)

tv.grid(column=0, row=3, columnspan=3, pady=5)

btn_inserir.grid(column=0, row=4)
btn_deletar.grid(column=1, row=4)
btn_obter.grid(column=2, row=4)


# tv.insert('', 'end', values=(i, n, f))

app.mainloop()
