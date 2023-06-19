from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from janela import Ui_Janela
from random import randint
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from qthread import Worker
import sys
from time import sleep


class Janela(Ui_Janela):
    def __init__(self, MainWindow):
        super().setupUi(MainWindow)
        self.escolha = 0
        self.var_tempo = 10
        self.var_jogadas = 10
        self.var_pontos = 0
        self.pc = 0
        self.btn_papel.clicked.connect(self.papel)
        self.btn_pedra.clicked.connect(self.pedra)
        self.btn_tesoura.clicked.connect(self.tesoura)
        
    def papel(self):
        self.escolha = 1
        self.pixmap_jogador = QPixmap('papel1.png')
        self.imagem_jogador.setPixmap(self.pixmap_jogador)
        
    def pedra(self):
        self.escolha = 2
        self.pixmap_jogador = QPixmap('pedra.png')
        self.imagem_jogador.setPixmap(self.pixmap_jogador)
        
    def tesoura(self):
        self.escolha = 3
        self.pixmap_jogador = QPixmap('tesoura.png')
        self.imagem_jogador.setPixmap(self.pixmap_jogador) 
        
    def jogada_pc(self):
        self.escolha_pc = randint(1,3)
        if self.escolha_pc == 1:
            self.pixmap_pc = QPixmap('papel1.png')
        elif self.escolha_pc == 2:
            self.pixmap_pc = QPixmap('pedra.png')
        elif self.escolha_pc == 3:
            self.pixmap_pc = QPixmap('tesoura.png')
        self.imagem_pc.setPixmap(self.pixmap_pc)
        return self.escolha_pc
    
    def jogar(self):
        self.pc = self.jogada_pc()
            
    def tempo(self, t):
        self.var_tempo = t
        self.value_tempo.setText(f"{self.var_tempo}")
        self.var_jogadas = t
        self.value_jogadas.setText(f"{self.var_jogadas}")
        
    def pontos(self):
        if self.pc == self.escolha:
            pass
        elif self.pc != self.escolha:
            if self.escolha == 1 and self.pc == 2:
                self.var_pontos = self.var_pontos + 1
            elif self.escolha == 1 and self.pc == 3:
                self.var_pontos = self.var_pontos - 1
            elif self.escolha == 2 and self.pc == 3:
                self.var_pontos = self.var_pontos + 1
            elif self.escolha == 2 and self.pc == 1:
                self.var_pontos = self.var_pontos - 1
            elif self.escolha == 3 and self.pc == 1:
                self.var_pontos = self.var_pontos + 1
            elif self.escolha == 3 and self.pc == 2:
                self.var_pontos = self.var_pontos - 1
            elif self.escolha == 0:
                self.var_pontos = self.var_pontos - 1
        self.value_pontos.setText(f"{self.var_pontos}")
        self.escolha = 0
        self.imagem_jogador.setPixmap(QPixmap(''))

        
    def timer(self):
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker()
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.pc.connect(self.jogar)
        self.worker.jogar.connect(self.pontos)
        self.worker.progress.connect(self.tempo)
        # Step 6: Start the thread
        self.thread.start()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    JanelaEx = QtWidgets.QMainWindow()
    j = Janela(JanelaEx)
    JanelaEx.show()
    j.timer()
    sys.exit(app.exec_())