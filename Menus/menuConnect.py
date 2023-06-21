# menuConnect.py
from PyQt5.QtWidgets import QMainWindow
from analoggaugewidget import *
from athenasUtils import *
from speeduino import *

# Importar a classe Ui_MainWindow gerada do arquivo Python convertido
from ui_dashAthenas import *

class MenuConnect:
    def __init__(self, ui, speeduino, obd2):
        self.ui = ui
        self.cnt = 0
        self.comPort = ""
        self.device = "" # essa variavel verifica se esta comunicando com a speeduino ou com o ELM
        self.speeduino = speeduino
        self.obd2 = obd2

        # define as donfiguracoes de timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.run)
        self.timer.start(1000)  # Atualizar a cada 1000ms, ou 1 segundo

        self.ui.bntCheckPorts.clicked.connect(self.checkPorts)
        self.ui.bntConnect.clicked.connect(self.deviceConnect)
        self.ui.bntDisconnect.clicked.connect(self.deviceDisconnect)

    def run_Speeduino(self):
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
CLT: {self.speeduino.coolant}
Coolant: {self.speeduino.coolant}
                ''')
                self.ui.debugTextTermina.setPlainText(strDebufInfo)

    def run_obd(self):
        pass

    def run(self):
        pass

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

    # conecta em algum dispositivo...
    def deviceConnect(self):
        
        self.comPort = self.ui.comboBoxPortaCom.currentText() # pega a porta com
        if(self.comPort != "-" and self.comPort != ""):
            print(f"PORTA COM SELECIONADA: {self.comPort}") 
            self.device = self.ui.comboBoxDevice.currentText()

            if self.device == "OBD2":
                print("Conecta na OBD2")
                self.ui.debugTextTermina.setPlainText("Conecta na OBD2")
                self.obd2Connect()

            elif self.device == "SPEEDUINO":
                print("Conecta na SPEEDUINO")
                self.ui.debugTextTermina.setPlainText("Conecta na SPEEDUINO")
                self.speeduinoConnect()
            else:
                self.ui.debugTextTermina.setPlainText("DEVICE INVALIDO, Selecione um device")
                print("DEVICE INVALIDO")
        else:
            print("Porta com invalida")
            self.ui.debugTextTermina.setPlainText("ERROR!\r\r\n\n2 - Selecione uma porta COM para comunicar \r\r\n\n3 - Clique em conectar")

        # conecta em algum dispositivo...
    def deviceDisconnect(self):
        
        if self.device == "OBD2":
            print("deconecta na OBD2")
            self.ui.debugTextTermina.setPlainText("Fechando a conexao com a OBD2")
            self.obd2.close()

        elif self.device == "SPEEDUINO":
            print("deconecta da SPEEDUINO")
            self.ui.debugTextTermina.setPlainText("Fechando a conexao com a  SPEEDUINO")
            self.speeduino.close()
        else:
            self.ui.debugTextTermina.setPlainText("DEVICE INVALIDO, Selecione um device")
            print("DEVICE INVALIDO")

    def obd2Connect(self):
        self.obd2.connect(self.comPort)

        if self.obd2.connection_status:
            print(f"START - EXITO COM A COMUNICACAO NA OBD2")
            self.obd2.start()
        else:
            print(f"FALHA COM A COMUNICACAO OBD2")

    def speeduinoConnect(self):
        self.speeduino.connect(self.comPort)

        if (self.speeduino.connection_status == True):
            self.ui.debugTextTermina.setPlainText("OK! Comunicacao estabelecida com Speeduino!")    
        else:
            self.ui.debugTextTermina.setPlainText("ERROR! nao foi possível se conectar a Speeduino!")
