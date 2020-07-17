import os
from pathlib import Path

from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtCore import Qt, QSize
from PyQt5 import QtWidgets, uic
import sys


from add_note import Add_Note_Window


class Note_Window(QMainWindow):
    def __init__(self, email, name):
        super().__init__()
        self.email = email
        self.name = name
        self.notes_text = ""
        self.add_note_window = None
        #get notes
        if Path("notes.txt").exists():
            with open(Path("notes.txt"), 'r') as self.read_file:
                self.read_file_data = self.read_file.read().replace('\n', '')
                self.file_data = self.read_file_data.split(';;;;')
                self.file_data = self.file_data[:-1]
                self.length = len(self.file_data)
                for self.counter_one in self.file_data:
                    self.data_line_split = self.file_data[self.length-1].split(',,,,')
                        #self.counter_one.split(',,,,')
                    self.notes_text = self.notes_text + self.data_line_split[0] + '\n' + self.data_line_split[1] + '\n\n\n'
                    self.length = self.length - 1
                if self.read_file_data.strip() == "":
                    self.notes_text = "You have not created any notes"

        else:
            self.create_file = open("notes.txt", "w")
            self.create_file.write("")
            self.notes_text = "You have not created any notes"
        self.initUI()

    #set ui
    def initUI(self):
        self.setWindowTitle(self.name + "'s Notes")
        self.resize(611, 721)
        self.setStyleSheet("background-color:#ffffff;")

        self.label = QLabel(self)
        self.label.setGeometry(30, 30, 500, 30)
        self.label.setText(self.name + "'s Notes")
        self.label.setStyleSheet("font-size:20px;")

        self.scroll = QScrollArea(self)
        self.scroll.setGeometry(16, 60, 530, 560)
        self.scroll.setStyleSheet("border: 0.5px solid #ffffff;")
        self.widget = QWidget(self)
        self.vbox = QVBoxLayout()
        # self.vbox.setGeometry(550, 500)



        object =  QtWidgets.QTextBrowser(self)
        object.setStyleSheet("background:#ffffff; border: 0px solid #fffff;font-size:16px; line-height:19px;")
        object.setStyleSheet("margin-right:25px;font-size:15px;")
        object.setText(self.notes_text)
        self.vbox.addWidget(object)

        self.widget.setLayout(self.vbox)

        #scroll area properties
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.button_add = QPushButton("Add Note", self)
        self.button_add.move(30, 630)
        self.button_add.resize(190, 40)
        self.button_add.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_add.clicked.connect(self.add_note_action)

        self.button_refresh = QPushButton("Refresh", self)
        self.button_refresh.move(260, 630)
        self.button_refresh.resize(190, 40)
        self.button_refresh.setStyleSheet("background:#008b8b; font-size:19px; color:#ffffff; border-radius:3px;")
        self.button_refresh.clicked.connect(self.ref_window)

        self.show()

    def add_note_action(self):
        self.add_note_window = Add_Note_Window(self.email, self.name)
        self.add_note_window.show()


    def ref_window(self):
        #close old window and open a new window
        self.close()
        self.ref_window = Note_Window(self.email, self.name)
        self.ref_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Note_Window("","")
    window.show()
    app.exec_()


# This project was developed by Safat Jamil, email : safaetxamil@yahoo.com