import pyperclip
from screeninfo import get_monitors
from seleniumbase import Driver
from selenium import webdriver
import pyautogui
import time
import keyboard
import win32api
import win32con
import os
from PIL import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# 1 screen calego ekranu
# 2 screen zaznaczonego obszaru
# 3 przeczytanie tekstu z obrazu
# 4 przelozenie przeczytanego tekstu na path of exile 2 trade
# 5 klikniecie w przycisk search

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


def website_PATHOFTRADE():  # function to open the website
    # ur path to user data example "C:/Users/yourUserName/AppData/Local/Google/Chrome/User Data/"
    ud = "C:/Users/"your username"/AppData/Local/Google/Chrome/User Data/"

    driver = Driver(uc=True, browser="chrome", chromium_arg=[
        # open chrome with user data
        f"--user-data-dir={ud}", "--profile-directory=default"],
    )
    url = "https://www.pathofexile.com/trade2/search/poe2/Standard"
    monitors = get_monitors()
    if len(monitors) > 1:
        second_monitor = monitors[1]
        driver.set_window_position(second_monitor.x, second_monitor.y)
    driver.maximize_window()
    driver.get(url)

    # X-1658 Y 344 search input window coordinates
    # X-963 Y 700 search button window coordinates


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


def fullfill_website():
    x = -1658
    y = 344
    click(x, y)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    y = 413
    click(x, y)
    time.sleep(0.1)
    x = -963
    y = 700
    click(x, y)


def searched_capture(event):  # keybind to take a screenshot after pressing x
    if event.name == 'x':
        print("wcisnieto x")
        while (win32api.GetAsyncKeyState(win32con.VK_LBUTTON)) == 0:
            time.sleep(0.1)
        Screenshoot()


def szukaj(event):

    if event.name == 'z':
        print("znaleziono")
        print(img_to_text())
        website_PATHOFTRADE()
        fullfill_website()


keyboard.on_press(searched_capture)
keyboard.on_press(szukaj)


while 1:
    time.sleep(0.1)
if (os.path.exists("screen.png")):
    time.sleep(5)
    os.remove("screen.png")
    os.remove("searched.png")
