# menuConnect.py
from PyQt5.QtWidgets import QMainWindow
from analoggaugewidget import *
from athenasUtils import *
from speeduino import *

# Importar a classe Ui_MainWindow gerada do arquivo Python convertido
from ui_dashAthenas import *

class MenuConnect:
    def __init__(self, ui, speeduino):
        self.ui = ui
        self.cnt = 0
        self.comPort = ""
        self.speeduino = speeduino

        # define as donfiguracoes de timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(1000)  # Atualizar a cada 1000ms, ou 1 segundo

        self.ui.bntCheckPorts.clicked.connect(self.checkPorts)
        self.ui.bntConnect.clicked.connect(self.speeduinoConnect)

    def run(self):
            if (self.speeduino.connection_status == True & self.speeduino.received_data == True):
                strDebufInfo = ""
                strDebufInfo = (f'''
SPEEDUINO DATA:
CNT: {self.speeduino.CNT}
TPS: {self.speeduino.TPS}
Battery Voltage: {self.speeduino.battery10}
RPM: {self.speeduino.RPM}
MAP: {self.speeduino.MAP}
IAT: {self.speeduino.IAT}
Coolant: {self.speeduino.coolant}
                ''')
                self.ui.debugTextTermina.setPlainText(strDebufInfo)

    def checkPorts(self):
        available_ports = sorted(Speeduino.list_ports())

        # Verificar se a lista de portas está vazia
        if not available_ports:
            print("Erro: Nenhuma porta disponível!")
            self.ui.debugTextTermina.setPlainText("Erro: Nenhuma porta disponível!")
        else:
            print(f"Veririficando portas disponíveis.") 
            self.ui.debugTextTermina.setPlainText("Listando as portas disponíveis...")

            # Limpar quaisquer itens existentes na comboBox
            self.ui.comboBoxPortaCom.clear()

            # Adicionar os portas disponíveis na comboBox
            self.ui.comboBoxPortaCom.addItems(available_ports)
            self.ui.debugTextTermina.setPlainText("2 - Selecione uma porta COM para comunicar \r\r\n\n3 - Clique em conectar")

    def speeduinoConnect(self):
        self.comPort = self.ui.comboBoxPortaCom.currentText()
        print(f"Tentando se comunicar com a Speeduino na comparta: {self.comPort}")
        if(self.comPort != ""): 
            self.speeduino.connect(self.comPort)

            if (self.speeduino.connection_status == True):
                self.ui.debugTextTermina.setPlainText("OK! Comunicacao estabelecida com Speeduino!")    
            else:
                self.ui.debugTextTermina.setPlainText("ERROR! nao foi possível se conectar a Speeduino!")
        else:
            self.ui.debugTextTermina.setPlainText("ERROR!\r\r\n\n2 - Selecione uma porta COM para comunicar \r\r\n\n3 - Clique em conectar")