from tkinter import *
import os


app = Tk()
app.title('CFB Cursos')
app.geometry('500x300')

img_logo = PhotoImage(file=caminho)
l_logo = Label(app, image=img_logo)
l_logo.place(x=10, y=10)

app.mainloop()
