import pyautogui
import time

pyautogui.press("win")
pyautogui.write("chrome")
time.sleep(1)
# web.whatsap.compilepyautogui.click(x=230,y=245)
pyautogui.press("enter")
time.sleep(2)


pyautogui.write("https://web.whatsapp.com/")
pyautogui.press("enter")
time.sleep(2)


pyautogui.click(x=230,y=245)
time.sleep(10)
pyautogui.write("Tharanya")
pyautogui.press("enter")
time.sleep(3)


pyautogui.click(x=230,y=320)
time.sleep(5)


pyautogui.click(x=1525,y=810)
time.sleep(10)
pyautogui.write("Hi")
pyautogui.press("enter")
time.sleep(3)

pyautogui.hotkey("ctrl","w")
time.sleep(2)