from kiwoom.kiwoom import *

import sys
from PyQt5.QtWidgets import *

class UI_class():
    def __init__(self):
        print("UI_class 입니다")

        self.app = QApplication(sys.argv)

        self.Kiwoom = Kiwoom()

        self.app.exec_()