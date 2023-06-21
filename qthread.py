from PyQt5.QtCore import QObject, QThread, pyqtSignal
import sys
from time import sleep

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# Step 1: Create a worker class
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)
    pc = pyqtSignal()
    jogar = pyqtSignal()

    def run(self):
        for i in range(10, 0, -1):
            self.progress.emit(i)
            self.pc.emit()
            sleep(1.2)
            self.jogar.emit()
        self.finished.emit()