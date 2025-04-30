import pyautogui

# Move o mouse para a posição (100, 100) em 1 segundo
pyautogui.moveTo(100, 100, duration=1)

# Clica com o botão esquerdo do mouse na posição (200, 200)
pyautogui.click(200, 200)

# Digita uma mensagem como se fosse teclado
pyautogui.write("Olá, isso é um teste do pyautogui!", interval=0.1)

# Pressiona ENTER
pyautogui.press('enter')

# Pressiona Ctrl + S (atalho para salvar)
pyautogui.hotkey('ctrl', 's')

# Mostra a posição atual do cursor
import time
time.sleep(3)  # Dá tempo para mover o mouse
print(pyautogui.position())

# Tira um print da tela inteira e salva como imagem
screenshot = pyautogui.screenshot()
screenshot.save("tela.png")

# Procura a imagem 'botao.png' na tela e clica nela
localizacao = pyautogui.locateCenterOnScreen('botao.png', confidence=0.8)
if localizacao:
    pyautogui.click(localizacao)
pip install opencv-python
