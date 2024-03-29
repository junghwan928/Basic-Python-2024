# date : 20240205
# file : test38_pyqt5.py
# desc : Qt디자이너 만든 UI 연동

import sys
from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class qtwin_exam(QWidget):
    def __init__(self) -> None:
        super().__init__()
        uic.loadUi('./day06/TestApp.ui',self) #QtDesinger에서 만든 UI를 load
        # BUTTON에 대한 시그널 처리 
        self.btnStart.clicked.connect(self.btnStartClicked) # UI 파일내에 있는 위젯접근은 VScode상에서 색상으로 표시 x
        self.btnStop.clicked.connect(self.btnStopClicked)

    def btnStartClicked(self):
        print('시작버튼 클릭')
        self.lblstatus.setText('상태 : 동작 시작')
        QMessageBox.about(self, '동작', '***System Start***')
    
    def btnStopClicked(self):
        print('종료버튼 클릭')
        self.lblstatus.setText('상태 : 동작 중지')
        QMessageBox.about(self, '동작', '***System Stop***')
        


    # QWidget에 있는 closeEvent를 그대로 쓰면 그냥 닫힘
    # 닫을지 말지 한번더 물어보는 형태로 다시 구현 하고 싶음 (재정의: Override)
    def closeEvent(self, QCloseEvent) -> None: # X버튼 종료확인 (재정의:)
        re = QMessageBox.question(self,'종료 확인','종료 하실겁니까?', QMessageBox.Yes|QMessageBox.No)
        if re == QMessageBox.Yes: # 닫기
            QCloseEvent.accept()
        else:
            QCloseEvent.ignore()
        

    
if __name__ == '__main__':
    loop = QApplication(sys.argv)
    instance = qtwin_exam()
    instance.show()
    loop.exec_()