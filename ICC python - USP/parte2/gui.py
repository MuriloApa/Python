from tkinter import *

janela = Tk()
janela.title("Teste de janela")
texto = Label(janela, text="Teste de texto")
texto.grid(column=0, row=0)

janela.mainloop()