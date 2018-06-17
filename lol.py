# encoding: utf-8

import os
import time
import pyautogui

os.startfile(r"C:\Riot Games\League of Legends\LeagueClient.exe")
print ("Aguardando tela de Login")
time.sleep(20)
print("Colocando Usuário")
pyautogui.click(1033,229, duration=1.00) #posição Username
pyautogui.typewrite('seuusuario', 0.25)
time.sleep(1)
print("Colocando Senha")
pyautogui.click(1033,271, duration=1.00) #posicao password
pyautogui.typewrite('suasenha', 0.25)
time.sleep(1)
print ("Clicando em Iniciar Sessão")
pyautogui.click(1102,521, duration=1.00) #posicao password
print("Aguardando Jogo Abrir")
time.sleep(60)
print ("Clicando em Jogar ")
pyautogui.click(269,109, duration=1.00)
time.sleep(1)
print "Selecionando Modo Personalizado"
pyautogui.click(555,159, duration=1.00)
print "Selecionando Modo Alternando"
pyautogui.click(771,440, duration=1.00)
print "Confirmando Partida"
pyautogui.click(594,621, duration=1.00)
time.sleep(5)
print "Adicionando Bot 1"
pyautogui.click(920,264, duration=1.00)
time.sleep(1)
print "Adicionando Bot 2"
pyautogui.click(909,305, duration=1.00)
time.sleep(1)
print "Adicionando Bot 3"
pyautogui.click(915,351, duration=1.00)
time.sleep(1)
print "Adicionando Bot 4"
pyautogui.click(925,382, duration=1.00)
print "Adicionando Bot 5"
pyautogui.click(916,418, duration=1.00)
time.sleep(1)
print("Clicando em Inicar")
pyautogui.click(620,628, duration=1.00)
time.sleep(10)
print ("Banindo primeiro Campeão")
pyautogui.click(828,158, duration=1.00)
pyautogui.typewrite('LeBlanc', 0.25)
time.sleep(1)
pyautogui.click(484,196, duration=1.00)
pyautogui.click(686,565, duration=1.00)
time.sleep(2)
print ("Banindo segundo Campeão")
pyautogui.click(828,158, duration=1.00)
pyautogui.typewrite('Ahri', 0.25)
pyautogui.click(484,196, duration=1.00)
pyautogui.click(686,565, duration=1.00)
time.sleep(2)
print ("Banindo terceiro Campeão")
pyautogui.click(828,158, duration=1.00)
pyautogui.typewrite('Nocturne', 0.25)
pyautogui.click(484,196, duration=1.00)
pyautogui.click(686,565, duration=1.00)
time.sleep(2)
print ("Selecionando seu Campeão")
pyautogui.click(828,158, duration=1.00)
pyautogui.typewrite('Rengar', 0.25)
pyautogui.click(484,196, duration=1.00)
time.sleep(1)
pyautogui.click(686,565, duration=1.00)