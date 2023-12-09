from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import random

class my_window(QMainWindow):
    def __init__(self):
        super(my_window, self).__init__()
        self.setGeometry(500, 150, 0, 0)
        self.setWindowTitle('Roshambo Game')
        self.setToolTip('')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(1280, 720)
        self.setStyleSheet("background-image: url(background.jpg)")

        self.btn = QPushButton(self)
        self.btn.setText('start')
        self.btn.setFont(QFont('0', 15))
        self.btn.setStyleSheet("background-color: white")
        self.btn.move(self.width() // 2 - self.btn.width() // 2, self.height() // 2 - self.btn.height() // 2)
        self.btn.clicked.connect(self.soft)

        self.btn_Try_again = QPushButton(self)
        self.btn_Try_again.setText('Try again?')
        self.btn_Try_again.setFont(QFont('0', 15))
        self.btn_Try_again.setStyleSheet("background-color: white")
        self.btn_Try_again.hide()
        self.btn_Try_again.move(self.width() // 2 - self.btn.width() // 2, self.height() // 2 - self.btn.height() // 2)
        self.btn_Try_again.clicked.connect(self.try_again)

        self.text = QLabel(self)
        self.text.setGeometry(50, 30, 200, 50)
        self.text.setFont(QFont('0', 25))
        self.text.setAutoFillBackground(True)
        self.text.setAttribute(Qt.WA_TranslucentBackground, True)

        self.btn1 = QPushButton(self)
        self.btn1.setFont(QFont('0', 15))
        self.btn1.setGeometry(10, 130, 322, 322)
        self.btn1.setStyleSheet("QPushButton { border-image: url(Rock.png); }")
        self.btn1.hide()
        self.btn1.setProperty("choice", "rock")
        self.btn1.clicked.connect(self.soft)

        self.btn2 = QPushButton(self)
        self.btn2.setFont(QFont('0', 15))
        self.btn2.setGeometry(400, 130, 322, 322)
        self.btn2.setStyleSheet("QPushButton { border-image: url(paper.png); }")
        self.btn2.hide()
        self.btn2.setProperty("choice", "paper")
        self.btn2.clicked.connect(self.soft)

        self.btn3 = QPushButton(self)
        self.btn3.setFont(QFont('0', 15))
        self.btn3.setGeometry(810, 130, 322, 322)
        self.btn3.setStyleSheet("QPushButton { border-image: url(scissair.png); }")
        self.btn3.hide()
        self.btn3.setProperty("choice", "scissor")
        self.btn3.clicked.connect(self.soft)

        self.mediaPlayer = QMediaPlayer()
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(random.choice(['Game_Music_1.mp3','Game_Music_2.mp3','Game_Music_3.mp3','Game_Music_4.mp3']))))
        self.player_choice = None

    def soft(self):
        self.mediaPlayer.play()
        x = ['rock', 'paper', 'scissor']
        Computer = random.choice(x)
        sender = self.sender()
        self.player_choice = sender.property("choice")

        if sender.text() == 'start':
            self.btn.hide()
            self.btn1.show()
            self.btn2.show()
            self.btn3.show()
            self.text.setText('Choose')

        if sender.property("choice") == 'rock':
            if Computer == 'scissor':
                self.text.setText('You Win')
            elif Computer == 'paper':
                self.text.setText('You lost')
            else:
                self.text.setText('Draw')
            self.text.setGeometry(100, 70, 200, 50)
            self.text.setFont(QFont('0', 35))
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn_Try_again.show()
            print("Computer choice: " + Computer)

        if sender.property("choice") == 'paper':
            if Computer == 'rock':
                self.text.setText('You Win')
            elif Computer == 'scissor':
                self.text.setText('You lost')
            else:
                self.text.setText('Draw')
            self.text.setGeometry(100, 70, 200, 50)
            self.text.setFont(QFont('0', 35))
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn_Try_again.show()
            print("Computer choice: " + Computer)

        if sender.property("choice") == 'scissor':
            if Computer == 'paper':
                self.text.setText('You Win')
            elif Computer == 'rock':
                self.text.setText('You lost')
            else:
                self.text.setText('Draw')
            self.text.setGeometry(100, 70, 200, 50)
            self.text.setFont(QFont('0', 35))
            self.btn1.hide()
            self.btn2.hide()
            self.btn3.hide()
            self.btn_Try_again.show()
            print("Computer choice: " + Computer)

    def try_again(self):
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(random.choice(['Game_Music_1.mp3','Game_Music_2.mp3','Game_Music_3.mp3','Game_Music_4.mp3']))))
        self.mediaPlayer.play()
        self.btn_Try_again.hide()
        self.btn1.show()
        self.btn2.show()
        self.btn3.show()
        self.text.setText('Choose')

def window():
    app = QApplication(sys.argv)
    win = my_window()
    win.show()
    sys.exit(app.exec_())
window()