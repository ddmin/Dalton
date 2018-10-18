from selenium import webdriver
import pyautogui
import time

def screenshot():
    pyautogui.PAUSE= 1
    pyautogui.FAILSAFE = True

    chromedriver =  r'C:\Users\ddmin\Downloads\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.desmos.com/calculator")

    pyautogui.moveTo(1235, 25)
    pyautogui.click()

    pyautogui.moveTo(100, 300)
    pyautogui.click()

    pyautogui.hotkey('ctrl', 'v')

    pyautogui.hotkey('fn', 'f11')
    time.sleep(5)

    pic = pyautogui.screenshot()

    pyautogui.hotkey('fn', 'f11')

    pic.save('graph.png')

    pyautogui.hotkey('ctrl', 'w')
    pyautogui.hotkey('ctrl', 'w')


