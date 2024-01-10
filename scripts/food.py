from time import sleep
import button
import keyboard
import pyautogui
import cv2
import pytesseract
import pyscreeze
import winsound
import win32gui

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pxg_title = "PokeXGames"

FOOD1_POS = 529, 630
FOOD2_POS = 569, 632
POS_AMARELA = 1454, 363, 28, 8
POS1_BATTLE = 1407, 381, 21, 14
POS1_VIDA = 1458, 392, 10, 6

SAFE = False

VIDA_AMARELA = 'pokexgames/vida_amarela.png'
MOB1 = 'pokexgames/elder.png'
MOB_BATTLE = 'pokexgames/para.png'
DEF_BATTLE = 'pokexgames/def_battle.png'
FOOD_EAT = 'pokexgames/magikarp.png'
VIDA_1 = 'pokexgames/vida1.png'

def food():
    pyautogui.moveTo(FOOD1_POS)
    pyautogui.click()
    pyautogui.moveTo(FOOD2_POS)
    pyautogui.click()

food()