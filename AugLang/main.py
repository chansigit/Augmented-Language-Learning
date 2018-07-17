#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys,os,tempfile
from PyQt5.Qt import QApplication, QClipboard
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPlainTextEdit
from PyQt5.QtCore import QSize
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import QSound,QMediaPlayer,QMediaContent

import PyQt5.QtCore as C
import PyQt5.QtMultimedia as M

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QUrl
from PyQt5 import QtMultimedia
from PyQt5.QtCore import Qt, QUrl

from googletrans import Translator
from yandex_speech import TTS
translator = Translator(service_urls=['translate.google.cn',])

sampleText="""Курс "Общие вопросы патологии и патологической анатомии" предназначен только для студентов, обучающихся на медицинских специальностях и медицинских специалистов. Предупреждение: данный курс содержит материалы, не рекомендованные к просмотру лицам со слабой психикой и беременным женщинам.Курс базируется на многолетнем опыте научной, диагностической и преподавательской работы автора в традициях известной научной школы. Изложение сложного материала проводится на современном уровне, все основные положения иллюстрируются большей частью оригинальными авторскими макро- и микроскопическими изображениями, схемами и рисунками\n"""




class ExampleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(880, 640))    
        self.setWindowTitle("苏维埃社会主义语言学习机") 

        # Add text field
        self.txtEdit = QPlainTextEdit(self)
        self.txtEdit.insertPlainText(sampleText)
        self.txtEdit.move(40,10)
        self.txtEdit.resize(800,300)

        # Add button
        self.btn1 = QPushButton("学习一个 (F1)", self)
        self.btn1.move(40,310)
        self.btn1.clicked.connect(self.button1Clicked)
        # Add button
        self.btn2 = QPushButton("念洋文 (F2)", self)
        self.btn2.move(160,310)
        self.btn2.clicked.connect(self.button2Clicked)

        # Add label
        self.lbl = QTextEdit(self)
        self.lbl.setReadOnly(True)
        self.lbl.move(40,340)
        self.lbl.resize(800,200)


        self.tts = TTS("jane", "mp3", "ae918646-fa47-4e66-96b6-6ce44d6d3146")
        self.player = QtMultimedia.QMediaPlayer(self)
        self.show()


    def button1Clicked(self):
        sender = self.sender()
        chosen= self.txtEdit.textCursor().selectedText()
        translated =translator.translate(chosen.strip(), dest='en')
        self.lbl.setText(translated.text)

    def button2Clicked(self):
        chosen= self.txtEdit.textCursor().selectedText()
        if chosen.strip()=="":
            return

        try:
            self.tts.generate(chosen.strip())
        except SSLError:
            pass
        self.tts.save(os.path.join(tempfile.gettempdir(),"tmp.mp3"))
        self.sound = QtMultimedia.QMediaContent(QUrl.fromLocalFile(os.path.join(tempfile.gettempdir(),"tmp.mp3")))
        self.player.setMedia(self.sound)
        self.player.setVolume(100)
        self.player.play()
        
        #QSound("tmp.mp3").play()


    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F1:
            chosen= self.txtEdit.textCursor().selectedText()
            translated =translator.translate(chosen.strip(), dest='en')
            self.lbl.setText(translated.text)
        elif e.key() == Qt.Key_F2:
            chosen= self.txtEdit.textCursor().selectedText()
            self.tts.generate(chosen.strip())
            self.tts.save("tmp.mp3")
            QSound(r"tmp.mp3").play()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = ExampleWindow()
    #mainWin.show()
    sys.exit( app.exec_() )