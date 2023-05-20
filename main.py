import os
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from analoggaugewidget import *
from athenasUtils import *
from Menus.menuGauges import MenuGauges
from Menus.menuConnect import MenuConnect
from speeduino import *

# Importar a classe Ui_MainWindow gerada do arquivo Python convertido
from ui_dashAthenas import *

# Classe MainWindow herdando QMainWindow
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)

        # Configurar a janela principal da interface do usuário
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # define as donfiguracoes de timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.mainPageRun)
        self.timer.start(250)  # Atualizar a cada 1000ms, ou 1 segundo

        self.speeduino = Speeduino()

        self.menuGauges = MenuGauges(self.ui, self.speeduino)
        self.menuConnect = MenuConnect(self.ui, self.speeduino)

        # utilizo isso aqui para saber em qual pagina esta atualmente
        self.currentPage = None

        # valor do contador de teste
        self.myValue = 1
        self.toggleValue = 0

        # Conectar botões às páginas correspondentes
        self.ui.btnPage1.clicked.connect(self.to_page_1)
        self.ui.btnPage2.clicked.connect(self.to_page_2)
        self.ui.btnPage3.clicked.connect(self.to_page_3)
        
        # Conectar botão de retorno à página principal
        self.ui.bntReturn_1.clicked.connect(self.to_main_page)
        self.ui.bntReturn_2.clicked.connect(self.to_main_page)
        self.ui.bntReturn_3.clicked.connect(self.to_main_page)

    def mainPageRun(self):
        if self.currentPage == 1:
            if self.speeduino.connection_status == True:
                self.ui.labelComStatus.setText("ON")
                self.ui.labelComStatus.setStyleSheet("background-color: green;")
                
                if self.speeduino.received_data == True:
                    self.ui.labelComCnt.setText(f"{self.speeduino.CNT}")
            else:
                self.ui.labelComStatus.setText("OFF")
                self.ui.labelComStatus.setStyleSheet("background-color: red;")
                self.ui.labelComCnt.setText(f"-")

    def to_page_1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)
        self.currentPage = 1

        
        # self.menuConnect = MenuConnect(self.ui) # poderia instanciar o menu quando for utilizar ele para otimizar

    def to_page_2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        self.currentPage = 2

    def to_page_3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
        self.currentPage = 3
        # self.menuGauges = MenuGauges(self.ui) # poderia instanciar o menu quando for utilizar ele para otimizar

    def to_main_page(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_0_main)

# Ponto de entrada do aplicativo
if __name__ == '__main__':
    # Criar uma instância do QApplication
    app = QApplication(sys.argv)
    
    # Criar e exibir a janela principal
    window = MainWindow()
    window.show()
    
    # Executar o loop de eventos principal do aplicativo
    sys.exit(app.exec_()) 
