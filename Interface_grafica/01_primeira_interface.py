from tkinter import *

primeira_janela = Tk()  # Objeto da classe Tk()
primeira_janela.title('CFB Cusros')
primeira_janela.geometry('500x300')  # largura x altura
primeira_janela.configure(background='#01a')
txt1 = Label(primeira_janela, text='Curso de Python', background='#01a', foreground='#fff')  # Criação do Lable
txt1.place(x=10, y=10, width=150, height=30)  # Isso é o que fara o Labre aparecer com seu tamanho e posição

v_txt = 'Módulo TKinter'
v_bg = '#ff0'
v_fg = '#000'
txt2 = Label(primeira_janela, text=v_txt, bg=v_bg, fg=v_fg)
txt2.pack(ipadx=20, ipady=20, padx=5, pady=5, side='top', fill=X, expand=True)


primeira_janela.mainloop()  # Loop que faz a janela ficar aparecendo na tela
