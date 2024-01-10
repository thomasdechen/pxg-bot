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


def move(location):
    x, y = pyscreeze.center(location)
    pyautogui.moveTo(x, y)

def move_and_click(location):
    move(location)
    pyautogui.click()

def revive():
    sleep(0.1)
    fearow = pyautogui.locateOnScreen("prints/poke_1.PNG", confidence = 0.75)
    try:
        pyautogui.moveTo(fearow)
    except:
        pass
    pyautogui.click()
    sleep(0.4)
    keyboard.pressonetime(button.key['M'], 0.4)
    sleep(0.3)
    pyautogui.click()

def player_alert():
    pos1 = pyautogui.locateOnScreen(MOB_BATTLE, confidence=0.70, region=(POS1_BATTLE), grayscale=False)
    vida = pyautogui.locateOnScreen(VIDA_1, confidence=0.5, region=(POS1_BATTLE), grayscale=True)
    if vida != None:
        print(1);
        if pos1 == None:
            winsound.Beep(2000, 1000)
            print(2);


def lootear():
    pyautogui.moveTo(800, 450)
    # list_pos = ['pos_fearow/pos_0.PNG', 'pos_fearow/pos_1.PNG',
    #             'pos_fearow/pos_2.PNG', 'pos_fearow/pos_3.PNG']
    list_pos = ['pokexgames/fearow.PNG', 'pokexgames/fearow2.PNG',
                'pokexgames/fearow3.PNG', 'pokexgames/fearow4.PNG', 'pokexgames/fearow5.PNG']
    for image in list_pos:
            check = pyautogui.locateOnScreen(image, confidence=0.80, region=(0, 0, 1600, 900))
            sleep(0.1)
            if check != None:
                break
    x_fear, y_fear = pyscreeze.center(check)
    # pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
    pyautogui.moveTo(x_fear+8, y_fear+40)
            # else:
            #     for image in list_pos:
            #         check = pyautogui.locateOnScreen(image, confidence=0.80)
            #         if check != None:
            #             x_fear, y_fear = pyscreeze.center(check)
            #             pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
    pyautogui.click()
    revive()
    sleep(0.07)
    keyboard.pressonetime(button.key['E'], 1)

hk_combo1 = ['F5', 'F7', 'F6']
hk_combo2 = ['F2', 'F4', 'F3', 'F1']


def atack(hotkey, delay=0.6):
    for item in hotkey:
        keyboard.press(button.key[item], delay)


def combo1():
    atack(hk_combo1)


def combo2():
    atack(hk_combo2)


def lock_enemy(enemy):
    pyautogui.moveTo(1470, 385)
    pyautogui.click()


def batalha():
    check_enemy = pyautogui.locateOnScreen(
        'prints/parasect.PNG', confidence=0.80, region=(180, 80, 1600, 900))
    if check_enemy != None:
        print(check_enemy)
        keyboard.pressonetime(button.key['F10'], 0.4)
        combo1()
        pyautogui.moveTo(800, 450)
        player_alert()
        check_enemy2 = pyautogui.locateOnScreen(
            'prints/parasect.PNG', confidence=0.80, region=(180, 80, 1600, 900))
        print('enemy2')
        print(check_enemy2)
        try:
            lock_enemy(check_enemy2)
        except:
            pass
        # if check_enemy2 != None:
        #     print(check_enemy2)
        #     combo2()
        #     player_alert()
        pyautogui.moveTo(1200, 450)
        sleep(0.05)
        lootear()
    pass