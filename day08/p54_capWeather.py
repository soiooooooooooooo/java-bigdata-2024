# file: p54_capWeather.py
# desc: 네이버 날씨화면 캡쳐

import pyautogui as auto
import pyperclip as clip
import time

regions = ['서울','강원','대전','대구','부산']
#auto.mouseInfo() # 251,112
for region in regions:
    auto.moveTo(251,112,duration=0.5)
    auto.leftClick()
    for _ in range(5):
        auto.press('backspace')
    time.sleep(0.2)

    clip.copy(f'{region} 날씨')
    auto.hotkey('ctrl','v') # 붙여넣기
    time.sleep(0.2)

    auto.press('enter') # '\n'도 가능
    time.sleep(1.0)
    #33,223 #700,897

    startX, startY = 33,223
    endX,endY = 700,897
    auto.screenshot(f'./day08/{region} 날씨.png',region=(startX,startY,endX-startX,endY-startY))
    print('저장완료!')