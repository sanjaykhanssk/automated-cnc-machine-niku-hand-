import pyautogui
import subprocess
import time
import pyperclip

subprocess.Popen([r"D:\Program Files\Benbox\3.7.99\bin\benbox.exe"])
time.sleep(10)
locate=pyautogui.locateCenterOnScreen('ben1.png')
image = str("sridevi.jpg")
pyautogui.click(locate)
time.sleep(5)

pyperclip.copy(image)

pyautogui.hotkey('ctrl','v')
time.sleep(3)
pyautogui.press('enter')

time.sleep(5)
#point=(945, 512)
pyautogui.click(783,492)
"""pyautogui.scroll(-10,point)
pyautogui.scroll(-10,point)
pyautogui.scroll(-10,point)
time.sleep(3)
pyautogui.scroll(-10,point)
pyautogui.scroll(-10,point)
pyautogui.scroll(-10,point)"""
"""count=0
while count==10:
    pyautogui.scroll(-10,point)
    time.sleep(3)
    count +=1"""
for _ in range(1,11):
    pyautogui.scroll(-10)