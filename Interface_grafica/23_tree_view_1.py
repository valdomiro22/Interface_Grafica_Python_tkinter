from tkinter import *
from tkinter import ttk

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

lista_nomes = [['1', 'Bertilda', '48549'], ['2', 'Vania', '3333349'], ['3', 'Andradonilda', '48544444']]

tv = ttk.Treeview(app, columns=('id', 'nome', 'fone'), show='headings')
tv.column('id', minwidth=0, width=50)
tv.column('nome', minwidth=0, width=250)
tv.column('fone', minwidth=0, width=100)

tv.heading('id', text='ID')
tv.heading('nome', text='NOME')
tv.heading('fone', text='TELEFONE')
tv.pack()

# tv.insert('', 'end', values=('10', 'bruno', '12'))
for (i, n, f) in lista_nomes:
    tv.insert('', 'end', values=(i, n, f))

app.mainloop()
