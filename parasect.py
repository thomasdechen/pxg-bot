import threading
from time import sleep
import button
import keyboard
import pyautogui
import cv2
import pytesseract
import pyscreeze
import winsound
import win32gui


# Importação de scripts
from scripts.perigo import perigo
from scripts.batalha import batalha
from scripts.batalha import player_alert
from scripts.food import food


pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pxg_title = "PokeXGames"

FOOD1_POS = 529, 630
FOOD2_POS = 569, 632
POS_AMARELA = 1454, 363, 28, 8
POS1_BATTLE = 1407, 381, 21, 14
POS1_VIDA = 1458, 392, 10, 6

SAFE = False

VIDA_AMARELA = 'pokexgames/vida_amarela.png'
DEF_BATTLE = 'pokexgames/def_battle.png'
VIDA_1 = 'pokexgames/vida1.png'

#Config
FOOD_EAT = 'config/food_img.png'
MOB1 = 'config/first_name.png'
MOB_BATTLE = 'config/mob_battle_img.png'
MOB_HUNT = 'prints/parasect.PNG'
POKE1 = "prints/poke_1.PNG"


bot_paused = False


def move(location):
    x, y = pyscreeze.center(location)
    pyautogui.moveTo(x, y)

def checkvida():
    px = pyscreeze.pixel(1520, 366)
    if px == (16, 16, 16):
        return True
    else:
        return False

def move_and_click(location):
    move(location)
    pyautogui.click()


def make_noise():
    duration = 100  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)

def defesa(defes):
    defes = defes+1

while True:
    window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if pxg_title in window_title:
        for index in range(11):
            while True:
                cv = False
                position_in_map = pyautogui.locateOnScreen(
                    './parasect/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
                if position_in_map == None:
                    position_in_map = pyautogui.locateOnScreen(
                    './parasect/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
                    break
                try:
                    move_and_click(position_in_map)
                except:
                    pass
                keyboard.pressonetime(button.key['F12'], 2)
                defe = 0
                perigo()
                checkvida()
                while position_in_map != None and checkvida() == False:
                    player_alert()
                    perigo()
                    position_in_map = pyautogui.locateOnScreen(
                        './parasect/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
                    SAFE = checkvida()
                    sleep(1)
                    checkvida()
                    if checkvida() == True:
                        cv = True
                    defe = defe + 1
                    if defe >= 2:
                        keyboard.pressonetime(button.key['F8'], 2)
                    if SAFE == True:
                        keyboard.press(button.key['S'])
                if cv == True:  
                    keyboard.press(button.key['W'])
                if SAFE == False:
                    sleep(2.5)
                elif SAFE == True:
                    sleep(1.2)
                if index == 10:
                    sleep(1)
                #keyboard.pressonetime(button.key['L'], 0.1)
                keyboard.pressonetime(button.key['Q'], 0.1)
                batalha()
                food()
                break