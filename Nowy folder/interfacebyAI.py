import pyperclip
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter.filedialog import *
import pyautogui
import time
import keyboard
import win32api
import win32con
import os
from PIL import Image
import pytesseract as tess
from screeninfo import get_monitors

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 1 screen calego ekranu
# 2 screen zaznaczonego obszaru
# 3 przeczytanie tekstu z obrazu
# 4 przelozenie przeczytanego tekstu na path of exile 2 trade
# 5 klikniecie w przycisk search

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def click(x, y):  # click function
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    print("clicked")


def Screenshoot():  # function to take a screenshot
    x, y = pyautogui.position()  # get position of the mouse
    print("taking a good photo")
    while (win32api.GetAsyncKeyState(win32con.VK_LBUTTON)):
        time.sleep(0.1)
    x1, y1 = pyautogui.position()  # get second position of the mouse
    if x1 < x:
        x, x1 = x1, x
    if y1 < y:
        y, y1 = y1, y
    # takes a screenshot of the selected area
    searched = pyautogui.screenshot(region=(x, y, x1-x, y1-y))
    searched.save("searched.png")  # save the screenshot
    print("good photo taken")  # confirmation of the screenshot
    return searched


def img_to_text():  # function to convert image to text
    img = Image.open("searched.png")
    new_size = tuple(4*x for x in img.size)  # resize image
    img = img.resize(new_size)
    text = tess.image_to_string(img)  # image to string
    text = ''.join(filter(lambda x: x.isalnum()  # specify the characters you want to keep
                          or x.isspace(), tess.image_to_string(img)))
    texts_list = text.split()
    text = " ".join(texts_list)
    pyperclip.copy(text)
    return text


def website_PATHOFTRADE():  # function to open the website
    # ur path to user data example "C:/Users/yourUserName/AppData/Local/Google/Chrome/User Data/"
    ud = "C:/Users//AppData/Local/Google/Chrome/User Data/"

    driver = Driver(uc=True, browser="chrome", chromium_arg=[
        # open chrome with user data
        f"--user-data-dir={ud}", "--profile-directory=default"],
    )

    # Close the previous tab if one is already opened
    if len(driver.window_handles) > 1:
        driver.switch_to.window(driver.window_handles[0])
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    # Open the new URL
    url = "https://www.pathofexile.com/trade2/search/poe2/Standard"
    monitors = get_monitors()
    if len(monitors) > 1:
        second_monitor = monitors[1]
        driver.set_window_position(second_monitor.x, second_monitor.y)
    driver.maximize_window()
    driver.get(url)

    # Wait for the element to be present and interactable
    wait = WebDriverWait(driver, 10)
    sciezka = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="trade"]/div[4]/div/div[1]/div[1]/div/div[2]/input')))

    print("znaleziono sciezke")
    input_text = img_to_text()
    sciezka.send_keys(input_text)


def szukaj():
    Screenshoot()
    print("znaleziono")
    print(img_to_text())
    website_PATHOFTRADE()


mybutton = tk.Button(text="szukaj", command=szukaj, font=10)
canvas1.create_window(150, 150, window=mybutton)

root.mainloop()

if os.path.exists("screen.png"):
    time.sleep(5)
    os.remove("screen.png")
    os.remove("searched.png")
