# file: p55_katalkAuto.py
# desc: 카톡pc에서 자동으로 메시지 보내기
#       pyautogui.ImageNotFoundException 예외 자주 발생

import pyautogui as auto
import pyperclip as clip
import os
import time

katalkLoc = auto.locateOnScreen('./day08/findLoc.png')
print(katalkLoc)
clickPos = auto.center(katalkLoc)
auto.doubleClick(clickPos)
time.sleep(0.5)

groupLoc = auto.locateOnScreen('./day08/findLoc2.png')
clickPos = auto.center(groupLoc)
auto.doubleClick(clickPos)
time.sleep(0.2)

clip.copy('파이썬에서 자동으로 보내는 메시지입니다.')
auto.hotkey('ctrl','v')
auto.press('\n')