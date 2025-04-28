import win32api
import win32con
import time
while 1:
    if win32api.GetAsyncKeyState(win32con.VK_LBUTTON):
        print("clicked")
        time.sleep(0.1)
