import keyboard
import time
from PIL import ImageGrab
# 不会打印任何东西,程序处于阻塞状态
class RecGt(object):
    def screen(self):
        if not keyboard.wait(hotkey='f1'):
            if not keyboard.wait(hotkey='ctrl+c'):
                time.sleep(0.01)
                image=ImageGrab.grabclipboard()
                image.save('test.png')

