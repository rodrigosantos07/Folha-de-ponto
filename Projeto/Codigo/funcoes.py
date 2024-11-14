import pyautogui
import pyperclip
import sys

import time

def capturaDeTela ():
    time.sleep(2)
    #ABRE O EXPLORADOR DE ARQUIVOS
    pyautogui.hotkey('win', 'e')
    time.sleep(1)
    #VAI PARA ABA DE NAVEGAÇÃO DO EXPLORADOR DE ARQUIVOS
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    #CAMINHO ONDE ESTÁ SALVO AS FOLHAS DE PONTO
    pyperclip.copy(r"C:\Users\MÁBIT-70\Documents\Folha-de-ponto\Projeto\Pontos")
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter') 
    
    #SELECIONA E ABRE O PDF FOLHA DE PONTO
    pyautogui.press('down')
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    #FECHA A ABA DE FERRAMENTAS
    pyautogui.press('Esc')
    time.sleep(1.5)
    #DIMINUI O ZOOM DO PDF
    pyautogui.hotkey('ctrl', '-')
    pyautogui.hotkey('ctrl', '-')
    time.sleep(1)
    #ACIONA O SCROLL DO MOUSE PARA POSICIONAR NO CENTRO DA TELA
    pyautogui.moveTo(500, 150)
    pyautogui.scroll(-50)
    time.sleep(1)
    #REALIZA CAPTURA DE TELA DA FOLHA DE PONTO
    pyautogui.press('prtsc')
    pyautogui.moveTo(x=376, y=157)
    time.sleep(1)
    pyautogui.mouseDown()
    pyautogui.moveTo(x=718, y=707)
    time.sleep(1)
    pyautogui.click()
    pyautogui.hotkey('ctrl','c')
    #FECHA O PDF
    time.sleep(1)
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    #FECHA O EXPLORADOR DE ARQUIVOS
    time.sleep(1.5)
    pyautogui.press('f4')
    pyautogui.keyUp('alt')  

#ACESSA O PERFIL CHROME QUE ESTÁ LOGADA A CONTA MABIT mabit.dp@gmail.com
def perfilChrome():
    time.sleep(1)
    #ABRE O EXPLORADOR DE ARQUIVOS E SELECIONA A ABA DE NAVEGAÇÃO
    pyautogui.hotkey('win', 'e')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(1)
    #COPIA O CAMINHO DO ATALHO DO PERFIL CHROME
    pyperclip.copy(r"C:\Users\MÁBIT-70\Documents\Folha-de-ponto\Projeto\Perfil chrome")
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    #ABRE O PERFIL CHROME E FECHA O EXPLORADOR DE ARQUIVOS
    pyautogui.write('PERFIL MABIT')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.hotkey('alt','tab')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')
    time.sleep(2)
    
#ACESSA A PLANILHA
def planilha():
    #ABRE O EXPLORADOR DE ARQUIVOS E ACESSA A ABA DE NAVEGAÇÃO
    pyautogui.hotkey('win','e')
    pyautogui.hotkey('ctrl','l')
    #COPIA O CAMINHO DA PLANILHA 
    pyperclip.copy(r"C:\Users\MÁBIT-70\Documents\Folha-de-ponto\Projeto\Planilha")
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    time.sleep(0.5)
    #ACESSA A PLANILHA E FECHA O EXPLORADOR DE ARQUIVOS
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.hotkey('alt','tab')
    time.sleep(0.5)
    pyautogui.hotkey('alt','f4')

def finalizarProcesso():
    sys.exit()

def pararProcesso():
    pyautogui.PAUSE = False

