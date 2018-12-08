import numpy as np
from PIL import ImageGrab # Windows and MacOS
# import pyscreenshot as ImageGrab # Linux
import cv2
import time
# import pyautogui
from directkeys import PressKey, ReleaseKey, R, X

def process_img(image):
    original_image = image
    # convert to gray
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # edge detection
    # processed_img =  cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def main():

    for i in list(range(2))[::-1]:
        print(i+1)
        time.sleep(1)

    last_time = time.time()
    while True:
        # PressKey(W)
        # screen =  np.array(ImageGrab.grab(bbox=(378,275,974,692)))    # Aim booster for my laptop
        screen =  np.array(ImageGrab.grab(bbox=(661,338,1261,759)))    # Aim booster for my PC
        #print('Frame took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        new_screen = process_img(screen)
        cv2.imshow('window', new_screen)
        #cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

main()
