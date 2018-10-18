from selenium import webdriver
import pyautogui
import time

def setup():
    chromedriver =  r'C:\Users\ddmin\Downloads\chromedriver.exe'
    driver = webdriver.Chrome(chromedriver)
    driver.get("https://www.desmos.com/calculator")

    pyautogui.moveTo(1235, 25)
    pyautogui.click()

    pyautogui.hotkey('fn', 'f11')
    time.sleep(5)

def screenshot():
    pyautogui.moveTo(75, 200)
    pyautogui.click()
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    pic = pyautogui.screenshot()

    pyautogui.moveTo(560, 190)
    pyautogui.click()

    pic.save('graph.png')
