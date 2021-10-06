from tkinter import *
import os


pasta_app = os.path.dirname(__file__)
caminho = pasta_app + '/logo.png'

app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

img_logo = PhotoImage(file=caminho)
l_logo = Label(app, image=img_logo)
l_logo.place(x=10, y=10)

app.mainloop()
