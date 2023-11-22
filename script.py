import sys
import time
import pyautogui
 
# final = pyautogui.hotkey('ctrl', 'v')

final = f'''Hey {sys.argv[1]}, \nHoping to add you to my list of professional networks :-)'''
pyautogui.typewrite(final)

