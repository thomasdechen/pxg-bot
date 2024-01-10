import pyautogui
from pynput.mouse import Listener


class Photo:
    def __init__(self):
        self.count = 0

    def take_photo(self, x, y):
        my_screen = pyautogui.screenshot(region=(x - 7, y - 7, 14, 14))
        path = 'fireantworker/flag_{}.png'.format(self.count)
        self.count = self.count + 1
        my_screen.save(path)

    def click(self, x, y, button, pressed):
        if button.name == 'right':
            return False
        if pressed:
            self.take_photo(x, y)


photo = Photo()

with Listener(on_click=photo.click) as listener:
    listener.join()
