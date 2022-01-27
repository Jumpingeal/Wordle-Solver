from ctypes.wintypes import BOOL, CHAR, INT
from turtle import color
from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

from wordle import *

def getBoxPos(xCoord: INT, yCoord: INT):
    """
    Converts X-Coord and Y-Coord to X and Y position of top left corner of grid
    """
    xPos = 67 * xCoord + 2
    yPos = 67 * yCoord + 2 + (yCoord // 2)      #This end bit accounts for every second gap being larger in y direction which is retarted and i hate whoever did this
    return xPos, yPos

def getLineColours(lineNum: INT, gridLocation):
    """
    Gets the color of the squares in the lineNum + 1 line, given the gridLocation as a list.
    """
    listCol = []
    pic = pyautogui.screenshot(region=(gridLocation))

    for i in range(5):
        xPos, yPos = getBoxPos(i, lineNum)
        xPos, yPos = xPos + 10, yPos + 10
        pixCol = pic.getpixel((xPos, yPos))

        if pixCol == (106,170,100):
            listCol.append('g')
        elif pixCol == (201,180,88):
            listCol.append('y')
        else:
            listCol.append('b')

    return listCol

if __name__ == '__main__':
    gridLocation = []

    while True:
        gridLocation = pyautogui.locateOnScreen('wordlegrid.png')
        if gridLocation != None:
            print(f'X: {str(gridLocation.left)}\nY: {str(gridLocation.top)}\nWidth: {str(gridLocation.width)}\nHeight: {str(gridLocation.height)}')
            break
        else:
            print('not found')

    sleep(4)
    
    

    #grey is 120, 124, 126
    #green is 106, 170, 100
    #yellow is 201, 180, 88 