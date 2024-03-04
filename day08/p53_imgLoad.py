# file: p53_imgLoag/py
# desc: PyAutoGui에서 이미지 읽어오기
import pyautogui as auto

#capImg = auto.locateOnScreen('./day08/screen.png') # 이미지 로드

auto.alert('테스트!!',title='pyAutoGui')
auto.confirm('계속 진행하겠습니까?')

text = auto.prompt('원하는 메시지 입력')
print(text)

pwd = auto.prompt('암호 입력')
print(pwd)