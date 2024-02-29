# file: p38_qtApp.py
# desc: PyQt5 QtDesigner를 같이 사용
'''
설치 > pip install PyQt5
설치 > pip install PyQt5Designer
'''
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 

class QtApp(QWidget):
    def __init__(self) -> None: 
        super().__init__() 
        self.initUI()
    
    def initUI(self): # ui파일을 로드해서 화면디자인 사용
        uic.loadUi('./day07/testThread.ui',self)
        self.setWindowTitle('노쓰레드앱')
        self.setWindowIcon(QIcon('./images/windows.png'))
        # 버튼 시그널 처리
        self.btnStart.clicked.connect(self.btnStartClicked) # ui파일내 위젯은 자동완성x

        self.show() 

    def btnMsgClicked(self):
        self.pgbTask.setValue(0) #재설정
        self.pgbTask.setRange(0,999_999) # 프로그레스바 범위설정
        self.btnStart.setDisabled(True)
        # UI(메인)스레드가 화면을 그릴 수 있는 여유가 없음(응답없음 발생)
        for i in range(0,1_000_000): #0~999,999
            print(f'노쓰레드 진행>> {i}')
            self.pgbTask.setValue(i)
            self.txbLog.append(f'노쓰레드 진행 >> {i}')
        self.btnStart.setEnabled(True)
        

    def closeEvent(self, QCloseEvent) -> None: # 우리식으로 오버라이드(재정의)
        re = QMessageBox.question(self,'종료확인','종료하시겠습니까?',QMessageBox.Yes|QMessageBox.Cancel)
        if re == QMessageBox.Yes: #진짜 닫음
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore() #무시


app = QApplication(sys.argv) #
inst = QtApp() # 객체 생성
app.exec_() #실행