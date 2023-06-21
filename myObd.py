# import serial
# import time
# import struct
# import serial.tools.list_ports
# import logging
# from PyQt5.QtCore import QThread, pyqtSignal
# import obd
# import time

# connection = obd.OBD("COM23")

# rpm_cmd = obd.commands.RPM
# battery_voltage_cmd = obd.commands.ELM_VOLTAGE

# while True:
#     rpm_response = connection.query(rpm_cmd)
#     battery_voltage_response = connection.query(battery_voltage_cmd)
    
#     if rpm_response.value is not None:
#         print(f"RPM: {rpm_response.value}")

#     if battery_voltage_response.value is not None:
#         print(f"Battery Voltage: {battery_voltage_response.value}")

#     time.sleep(0.5)  # pause for 500ms





import serial
import time
import struct
import serial.tools.list_ports
import logging
from PyQt5.QtCore import QThread, pyqtSignal
import obd
import time

class OBD2(QThread):

    DEBUG = False  # Configure como False para desativar a depuração

    rpm_signal = pyqtSignal(object)
    battery_voltage_signal = pyqtSignal(object)
    coolant_temp_signal = pyqtSignal(object)
    oil_pressure_signal = pyqtSignal(object)
    fuel_level_signal = pyqtSignal(object)
    speed_signal = pyqtSignal(object)

    def __init__(self):
        QThread.__init__(self)
        self.port = ""
        self.last_request_time = time.time()  # Variável para controlar o tempo de requisições
        self.TIME_REQUEST_DATA = 0.4  # tempo entre as solicitações de dados
        self.connection_status = False  # status de conexão com a OBD
        self.received_data = False  # se está recebendo dados ativamente
        self.ini_vars()

    def debug_print(self, msg):
        if self.DEBUG:
            print(msg)

    # caso a comunicação falhe, seta os dados para desconectar
    def setFailedComm(self, msg):
        self.debug_print(f"Falha na comunicação: {msg}")
        self.connection_status = False
        self.received_data = False

    # tenta conectar com OBD, pega os status e inicializa a thread...
    def connect(self, port):
        self.port = port
        try:
            self.debug_print(f"Conectando na porta: {self.port}")
            self.connection = obd.OBD(self.port)
            self.connection_status = True
            self.debug_print("Conexão estabelecida.")
        except Exception as e:
            self.connection_status = False
            self.debug_print("Falha ao comunicar")
            self.setFailedComm(str(e))

    # fica coletando os dados da OBD
    def run(self):
        self.debug_print("Iniciando coleta de dados...")

        while not self.isInterruptionRequested():
            if time.time() - self.last_request_time >= self.TIME_REQUEST_DATA:
                self.last_request_time = time.time()

                rpm_response = self.connection.query(obd.commands.RPM)
                battery_voltage_response = self.connection.query(obd.commands.ELM_VOLTAGE)
                coolant_temp_response = self.connection.query(obd.commands.COOLANT_TEMP)
                # oil_pressure_response = self.connection.query(obd.commands.OIL_PRESSURE)
                fuel_level_response = self.connection.query(obd.commands.FUEL_LEVEL)
                speed_response = self.connection.query(obd.commands.SPEED)

                if speed_response.value is not None:
                    self.speed_signal.emit(speed_response.value)
                    self.SPEED = speed_response.value.to("km/h").magnitude  # converte para km/h
                    self.debug_print(f"Velocidade: {self.SPEED}")
                    self.received_data = True

                if rpm_response.value is not None:
                    # self.debug_print(f"RPM: {rpm_response.value.magnitude}")
                    self.rpm_signal.emit(rpm_response.value)
                    self.RPM = rpm_response.value.magnitude
                    self.debug_print(f"RPM: {self.RPM}")
                    # self.debug_print(f"RPM: {self.RPM}")
                    self.received_data = True

                if battery_voltage_response.value is not None:
                    # self.debug_print(f"Tensão da Bateria Recebida: {battery_voltage_response.value}")
                    self.battery_voltage_signal.emit(battery_voltage_response.value)
                    self.BATTERY = battery_voltage_response.value.magnitude
                    self.debug_print(f"Tensão da Bateria: {self.BATTERY}")
                    self.received_data = True

                if coolant_temp_response.value is not None:
                    self.coolant_temp_signal.emit(coolant_temp_response.value)
                    self.COOLANT_TEMP = coolant_temp_response.value.magnitude
                    self.debug_print(f"Temperatura do Líquido de Arrefecimento: {self.COOLANT_TEMP}")
                    self.received_data = True

                self.OIL_PRESSURE
                # if oil_pressure_response.value is not None:
                #     self.oil_pressure_signal.emit(oil_pressure_response.value)
                #     self.OIL_PRESSURE = oil_pressure_response.value.magnitude
                #     self.debug_print(f"Pressão do Óleo: {self.OIL_PRESSURE}")
                #     self.received_data = True

                if fuel_level_response.value is not None:
                    self.fuel_level_signal.emit(fuel_level_response.value)
                    self.FUEL_LEVEL = fuel_level_response.value.magnitude
                    self.debug_print(f"Nível de Combustível: {self.FUEL_LEVEL}")
                    self.received_data = True

    def close(self):
        self.debug_print("Fechando conexão...")
        self.requestInterruption()
        self.wait()
        self.connection.close()

    def ini_vars(self):
        self.BATTERY = 0
        self.RPM = 0
        self.SPEED = 0
        self.COOLANT_TEMP = 0
        self.OIL_PRESSURE = 0
        self.FUEL_LEVEL = 0

    def getConnectionStatus(self):
        return self.connection_status

    def getReceivedDataStatus(self):
        return self.received_data
