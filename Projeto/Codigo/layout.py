import pyautogui
from tkinter import *
import sys
import funcoes

import principal

janela = Tk()
janela.title("CALCULAR FOLHA DE PONTO")
texto = Label(janela, text="==========CLIQUE PARA INICIAR==========")
texto.grid(column=0, row=0, padx=40, pady=40)

def iniciar():
    principal.telaPrincipal()
def fim():
    funcoes.finalizarProcesso()
def pause():
    funcoes.pararProcesso()

botao_iniciar = Button(janela, text="Iniciar", command=iniciar, bg='green')
botao_iniciar.grid(column=0, row=10, padx=15, pady=15)

botao_encerrar = Button(janela, text="Finalizar", command=fim, bg='red')
botao_encerrar.grid(column=0, row=1, padx=10, pady=10)

botao_pause = Button(janela, text="Parar", command=pause, bg='yellow')
botao_pause.grid(column=0, row=15, padx=15, pady=15)

janela.mainloop()