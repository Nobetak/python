import cv2 as cv
import numpy as np
import os
import win32gui, win32ui, win32con, win32api 
from time import time
from windowcapture import WindowCapture
from vision import Vision

wincap=WindowCapture('PathOfExileSteam')
vis=Vision('./exit.png')

loop_time =time()
while(True):

    screenshot = wincap.get_screenshot()
    print('fps {}'.format(1/(time()-loop_time)))
    vis.find(screenshot,0.67 ,debug_mode='rectangles')
    loop_time = time()
  
    if(cv.waitKey(1) == ord('q')):
        break

cv.destroyAllWindows()
print('done')
