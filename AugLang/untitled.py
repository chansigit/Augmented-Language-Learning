import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl
from PyQt5 import QtMultimedia
from PyQt5.QtCore import Qt, QUrl

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.player = QtMultimedia.QMediaPlayer(self)
        self.sound = QtMultimedia.QMediaContent(QUrl.fromLocalFile("/Users/chensj16/code/Augmented-Language-Learning/AugLang/tmp.mp3"))
        self.player.setMedia(self.sound)
        self.player.setVolume(100)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F1:
            self.player.play()



app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())