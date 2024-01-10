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
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

pxg_title = "PokeXGames"


BUSH = ['bush/bush-img/bush1.PNG', 'bush/bush-img/bush1.PNG', 'bush/bush-img/bush1.PNG']

right = (821,279,50,50)
left = (719,281,50,50)

def collect():
    for image in BUSH:
        bush = pyautogui.locateOnScreen(image, confidence=0.80, region=(340, 73, 950, 440))
        if bush != None:
            break
    x_bush, y_bush = pyscreeze.center(bush)
    # pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
    pyautogui.moveTo(x_bush+50, y_bush+0)
    pyautogui.click()
    for image in BUSH:
        bush = pyautogui.locateOnScreen(image, confidence=0.80, region=(right))
        bush = pyautogui.locateOnScreen(image, confidence=0.80, region=(left))
    while bush == None: # type: ignore
        for image in BUSH: # type: ignore
            bush = pyautogui.locateOnScreen(image, confidence=0.80, region=(right))
            bush = pyautogui.locateOnScreen(image, confidence=0.80, region=(left))
            print("Procurando bush")
            if bush != None:
                break
    x_bush, y_bush = pyscreeze.center(bush)
    pyautogui.moveTo(x_bush+0, y_bush+0)
    keyboard.press('F1')
    pyautogui.click()
    if bush == None:
        return False
    else:
        return True

while True:
    window_title = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if pxg_title in window_title:
        collect()
        if collect == False:
            for index in range(9):
                while True:
                    cv = False
                    position_in_map = pyautogui.locateOnScreen(
                        '.bush/map/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
                    if position_in_map == None:
                        position_in_map = pyautogui.locateOnScreen(
                        './map/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
                        break
                    try:
                        move_and_click(position_in_map)
                    except:
                        pass
