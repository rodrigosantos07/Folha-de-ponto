import pyautogui
import funcoes
import time


time.sleep(3)
def telaPrincipal():
    funcoes.planilha()
    time.sleep(3)
    funcoes.perfilChrome()    
    time.sleep(3)
    funcoes.capturaDeTela()
    time.sleep(1)
    
    #O NAVEGADOR DEVE ESTAR COM ZOOM EM 75%
    
    time.sleep(10)
    #CLICA NA ABA PRA ADICIONAR NOVA CAPTURA DE TELA DA FOLHA DE PONTO
    pyautogui.click(x=253, y=700)
    time.sleep(1)
    pyautogui.click()
    time.sleep(8)
    #COLA NOVA CAPTURA DE TELA DA FOLHA DE PONTO
    pyautogui.hotkey('ctrl','v')
    time.sleep(10)
    #INICIAR A LEITURA DA FOLHA DE PONTO
    pyautogui.click(x=1052, y=692)
    pyautogui.click()
    time.sleep(30)
    #COPIA O RESULTADO 
    pyautogui.click(x=243, y=218)
    pyautogui.click()
    time.sleep(1)
    pyautogui.click(x=243, y=260)
    time.sleep(1)
    pyautogui.click()
    pyautogui.click(x=243, y=282)
    time.sleep(1)
    pyautogui.click(x=243, y=366)
    time.sleep(1)
    pyautogui.click(x=243, y=408)
    time.sleep(1)
    pyautogui.click(x=243, y=443)
    time.sleep(1)
    pyautogui.click(x=243, y=486)
    time.sleep(1)
    pyautogui.click(x=243, y=570)
    time.sleep(1)
    pyautogui.click(x=243, y=608)
    time.sleep(1)
    pyautogui.click(x=243, y=620)
    time.sleep(1)
    pyautogui.click(x=243, y=525)
    pyautogui.click()
    pyautogui.click(x=333, y=308)
    time.sleep(1)
    pyautogui.click()
    time.sleep(2)
    #ACESSA A PLANILHA
    pyautogui.hotkey('alt', 'tab')
    time.sleep(1)
    pyautogui.click(x=28, y=228)
    time.sleep(2)
    pyautogui.click()
    time.sleep(2)
    #COPIA OS VALORES DA FOLHA DE PONTO
    pyautogui.hotkey('ctrl','v')
    time.sleep(2)
    pyautogui.click()
    pyautogui.click(x=1057, y=261)
    time.sleep(1)


