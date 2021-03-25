import pyautogui
import sys

from pymsgbox import *

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    alert(text='Vocë pressionou CTRL+C', title='Parada!', button='OK')
    print('\n')