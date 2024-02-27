# file: p35_qtApp.py
# desc: PyQt5 앱 만들기
'''
PyQt5 -> Qt를 파이썬에서 쓸 수 있도록 만든 라이브러리
Qt -> C,C++ 사용할 GUI(WinApp) 프레임워크(멀티플랫폼)

설치 > pip install PyQt5
'''
import sys
# QApplication 만들앱 전체관리 클래스, QWidget 메뉴가 없는 윈도우앱,QMainWindow 메뉴가 있는 윈도우앱
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

class QtApp(QWidget):# QWidget이 가지고있는 속성,변수,함수를 다 사용가능
    def __init__(self) -> None: 
        super().__init__() #생성자,부모클래스의 생성자 함수도 실행되어야
        self.setGeometry(300, 300, 800, 400) #바탕화면 정해진 위치에 넓이와 높이로 그릴설정
        self.setWindowTitle('첫번째 윈도우앱')
        self.show() #윈도우 창 그려!

app = QApplication(sys.argv) #
inst = QtApp() # 객체 생성
app.exec_() #실행