import pyautogui
import pyperclip

def CopyMousePos():
    pos = pyautogui.position()
    x = pos[0]
    y = pos[1]
    z = str(x) + ' , ' + str(y)
    pyperclip.copy(z)

CopyMousePos()
