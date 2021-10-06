from tkinter import *

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

lb_canal = Label(app, text='CFB Cursos')
lb_nome = Label(app, text='Digite seu nome:')
lb_idade = Label(app, text='Informe sua idade:')

et_nome = Entry(app)
et_idade = Entry(app)
et_nome.grid(column=1, row=1)
et_idade.grid(column=1, row=2)

btn = Button(app, text='Youtube')

lb_canal.grid(column=0, row=0, pady=20)
lb_nome.grid(column=0, row=1, sticky='e', padx=5)  # sticky: n s e w
lb_idade.grid(column=0, row=2, padx=10)

app.mainloop()
