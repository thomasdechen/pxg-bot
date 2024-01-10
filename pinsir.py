from time import sleep
import button
import keyboard
import pyautogui
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'


def move(location):
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y)


def move_and_click(location):
    move(location)
    pyautogui.click()


def lootear():
    pyautogui.moveTo(800, 450)
    list_pos = ['pos_fearow/pos_0.PNG', 'pos_fearow/pos_1.PNG',
                'pos_fearow/pos_2.PNG', 'pos_fearow/pos_3.PNG']
    for image in list_pos:
        check = pyautogui.locateOnScreen(image, confidence=0.80)
        if check != None:
            x_fear, y_fear = pyautogui.center(check)
            pyautogui.moveTo(x_fear+8, y_fear+9, 0.1)
    pyautogui.click()
    revive()
    sleep(2)
    keyboard.pressonetime(button.key['E'], 2)


def revive():
    sleep(0.1)
    fearow = pyautogui.locateOnScreen("prints/poke_1.PNG", confidence=0.75)
    try:
        x_fearow, y_fearow = pyautogui.center(fearow)
        pyautogui.moveTo(x_fearow, y_fearow, 0.1)
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
    im = pyautogui.screenshot(region=(168, 73, 22, 15))
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
        'prints/pinsir.PNG', confidence=0.80, region=[180, 80, 1600, 900])
    if check_enemy != None:
        print(check_enemy)
        keyboard.pressonetime(button.key['F10'], 0.4)
        combo1()
        sleep(1)
        pyautogui.moveTo(800, 450)
        check_enemy2 = pyautogui.locateOnScreen(
            'prints/pinsir.PNG', confidence=0.80, region=[180, 80, 1600, 900])
        print('enemy2')
        print(check_enemy2)
        if check_enemy2 != None:
            print(check_enemy2)
            lock_enemy(check_enemy2)
            keyboard.pressonetime(button.key['F10'], 0.4)
            combo2()
            sleep(1.5)
        pyautogui.moveTo(800, 450)
        sleep(1)
        lootear()
    pass


def defesa(defes):
    defes = defes+1


for index in range(8):
    while True:
        position_in_map = pyautogui.locateOnScreen(
            './pinsir/flag_{}.png'.format(index), confidence=0.80, region=(1396, 56, 200, 205))
        move_and_click(position_in_map)
        keyboard.pressonetime(button.key['F12'], 2)
        defe = 0
        while position_in_map != None:
            position_in_map = pyautogui.locateOnScreen(
                './pinsir/flag_{}.png'.format(index), confidence=0.70, region=(1396, 56, 200, 205))
            sleep(1)
            defe = defe + 1
            if defe >= 5:
                keyboard.pressonetime(button.key['F8'], 2)
        sleep(1.6)
        keyboard.pressonetime(button.key['L'], 0.1)
        keyboard.pressonetime(button.key['F11'], 0.1)
        batalha()
        break
