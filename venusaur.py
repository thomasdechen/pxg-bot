from time import sleep
import button
import keyboard
import pyautogui
import cv2
import pytesseract
import pyscreeze
import winsound
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

FOOD1_POS = 529, 630
FOOD2_POS = 569, 632
POS_AMARELA = 1454, 363, 28, 8
POS1_BATTLE = 1407, 381, 21, 14
POS1_VIDA = 1458, 392, 10, 6

SAFE = False

VIDA_AMARELA = 'pokexgames/vida_amarela.png'
MOB1 = 'pokexgames/brave.png'
MOB_BATTLE = 'pokexgames/venu.png'
DEF_BATTLE = 'pokexgames/def_battle.png'
FOOD_EAT = 'pokexgames/magikarp.png'
VIDA_1 = 'pokexgames/vida1.png'


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

def food():
    pyautogui.moveTo(FOOD1_POS)
    pyautogui.click()
    pyautogui.moveTo(FOOD2_POS)
    pyautogui.click()
    sleep(0.2)

def make_noise():
    duration = 100  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
    winsound.Beep(freq, duration)

def perigo():
    pos3 = pyautogui.locateOnScreen(VIDA_AMARELA, confidence=0.9, region=(POS_AMARELA), grayscale=False)
    if pos3 != None:
        return True
    else:
        return False

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
    list_pos = ['pos_fearow/pos_0.PNG', 'pos_fearow/pos_1.PNG',
                'pos_fearow/pos_2.PNG', 'pos_fearow/pos_3.PNG']
    for image in list_pos:
            check = pyautogui.locateOnScreen(image, confidence=0.80)
            if check != None:
                x_fear, y_fear = pyscreeze.center(check)
                pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
            # else:
            #     for image in list_pos:
            #         check = pyautogui.locateOnScreen(image, confidence=0.80)
            #         if check != None:
            #             x_fear, y_fear = pyscreeze.center(check)
            #             pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
    pyautogui.click()
    revive()
    sleep(1.5)
    keyboard.pressonetime(button.key['E'], 2)


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


def scima():
    pyautogui.moveTo((785, 195))
    pyautogui.middleClick()


def sbaixo():
    pyautogui.moveTo((784, 410))
    pyautogui.middleClick()


def sdireita():
    pyautogui.moveTo((891, 303))
    pyautogui.middleClick()


def sesquerda():
    pyautogui.moveTo((677, 303))
    pyautogui.middleClick()


def ssudeste():
    pyautogui.moveTo((935, 440))
    pyautogui.middleClick()


def ssudoeste():
    pyautogui.moveTo((645, 443))
    pyautogui.middleClick()


def stop1():
    sbaixo()


def stop2():
    scima()


def stop3():
    scima()


def stop4():
    scima()


def stop5():
    sbaixo()


def stop6():
    sdireita()


def stop7():
    sbaixo()


def stop8():
    sesquerda()


def moves():
    if index == 0:
        sbaixo()
    elif index == 1:
        ssudeste()
    elif index == 2:
        ssudeste()
    elif index == 3:
        ssudoeste()
    elif index == 4:
        ssudoeste()
    elif index == 5:
        sesquerda()
    elif index == 6:
        sesquerda()
    elif index == 7:
        scima()
    elif index == 8:
        ssudeste()
    elif index == 9:
        ssudeste()


def checar_vida():
    im = pyscreeze.screenshot(region=(168, 73, 22, 15))
    im.save('my_screenshot.png')
    im = cv2.imread('my_screenshot.png')
    text = pytesseract.image_to_string(im)
    print(text)
    try:
        text = int(text)
    except:
        pass
    try:
        if text > 50:
            print("tranquilo")
        elif text < 50:
            print("atacar")
            #check_position == None
            pass
    except:
        pass


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
        'prints/venusaur.PNG', confidence=0.80, region=(180, 80, 1600, 900))
    if check_enemy != None:
        print(check_enemy)
        keyboard.pressonetime(button.key['F10'], 0.4)
        combo1()
        sleep(1)
        pyautogui.moveTo(800, 450)
        player_alert()
        check_enemy2 = pyautogui.locateOnScreen(
            'prints/venusaur.PNG', confidence=0.80, region=(180, 80, 1600, 900))
        print('enemy2')
        print(check_enemy2)
        try:
            lock_enemy(check_enemy2)
        except:
            pass
        while check_enemy2 != None:
            print(check_enemy2)
            combo2()
            player_alert()
            check_enemy2 = pyautogui.locateOnScreen(
            'prints/venusaur.PNG', confidence=0.80, region=(180, 80, 1600, 900))
        pyautogui.moveTo(1200, 450)
        sleep(0.6)
        lootear()
    pass


def defesa(defes):
    defes = defes+1


while True:
    for index in range(11):
        while True:
            cv = False
            position_in_map = pyautogui.locateOnScreen(
                './venusaur/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
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
                    './venusaur/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
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
