import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QLineEdit
from PyQt5.QtCore import Qt
import sys
from c_odf import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TidyDownload")
        self.setLayout(QVBoxLayout())

        self.folderLabel = QLabel("Folder:")
        self.folderLineEdit = QLineEdit()
        self.folderButton = QPushButton("Browse")
        self.folderButton.clicked.connect(self.select_folder)

        self.layout().addWidget(self.folderLabel)
        self.layout().addWidget(self.folderLineEdit)
        self.layout().addWidget(self.folderButton)

        self.daysLabel = QLabel("Days:")
        self.daysLineEdit = QLineEdit()
        self.layout().addWidget(self.daysLabel)
        self.layout().addWidget(self.daysLineEdit)

        self.startButton = QPushButton("Start Cleanup")
        self.startButton.clicked.connect(self.start_cleanup)
        self.layout().addWidget(self.startButton)

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        self.folderLineEdit.setText(folder)

    def start_cleanup(self):
        cleanup_old_files(self.folderLineEdit.text(), int(self.daysLineEdit.text()))

app = QApplication(sys.argv)

demo = App()
demo.show()

sys.exit(app.exec_())