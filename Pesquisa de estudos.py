import pyautogui
import time



a = str(input("digite um assunto: "))
b = str(input("digite um assunto: "))
c = str(input("digite um assunto: "))
d = str(input("digite um assunto: "))
def pesquisa(k):
    pyautogui.press("win")
    time.sleep(8)
    pyautogui.click(x=661, y=324)
    time.sleep(8)
    pyautogui.click(x=747, y=62)
    pyautogui.write("youtube.com")
    pyautogui.press("enter")
    time.sleep(6)
    pyautogui.click(x=697, y=128)
    pyautogui.write(k)
    time.sleep(3)
    pyautogui.press("enter")
pesquisa(a)
time.sleep(30)
pesquisa(b)
time.sleep(30)
pesquisa(c)
