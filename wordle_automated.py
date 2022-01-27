from ctypes.wintypes import CHAR
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

from wordle import *

def getBoxPos():
    """
    Converts X-Box and Y-Box to X and Y position of top left corner of grid
    """


if __name__ == '__main__':
    gridLocation = []

    while True:
        gridLocation = pyautogui.locateOnScreen('wordlegrid.png')
        if gridLocation != None:
            print('X: ' + str(gridLocation.left) + '\nY: ' + str(gridLocation.top) + '\nWidth: ' + str(gridLocation.width) + '\nHeight: ' + str(gridLocation.height))
            break
    
    