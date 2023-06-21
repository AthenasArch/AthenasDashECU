import serial
import time
import struct
import serial.tools.list_ports
import logging
from PyQt5.QtCore import QThread, pyqtSignal
# https://wiki.speeduino.com/en/reference/Interface_Protocol

SPEEDUINO_CMD_A_CURR_STATUS = ('A', 120)
SPEEDUINO_CMD_S_SIGNATURE = ('S', 8)
SPEEDUINO_CMD_r_TUNING_PAGE = ('r', 192)
SPEEDUINO_CMD_w_WRITE_PAGE = ('w', 192)
SPEEDUINO_CMD_t_GET_TEMPERATURE = ('t', 8)
SPEEDUINO_CMD_d_GET_DATE = ('d', 8)
SPEEDUINO_CMD_f_GET_FREE_MEMORY = ('f', 4)
SPEEDUINO_CMD_i_GET_CANBUS_INFO = ('i', 8)
SPEEDUINO_CMD_n_GET_CANBUS_DETAILS = ('n', 8)
SPEEDUINO_CMD_o_SEND_CANBUS = ('o', 8)
SPEEDUINO_CMD_x_GET_CONFIG = ('x', 8)
SPEEDUINO_CMD_g_GET_AFR_TARGET = ('g', 8)
SPEEDUINO_CMD_y_GET_CONFIG2 = ('y', 8)
SPEEDUINO_CMD_z_SET_CONFIG2 = ('z', 8)

# Configurar o logging
logging.basicConfig(level=logging.DEBUG)

class SpeeduinoRequestThread(QThread):
    dataReceived = pyqtSignal(object)  # Signal to emit when data is received

    def __init__(self, speeduino):
        QThread.__init__(self)
        self.speeduino = speeduino
        print("Thread iniciada...")

    def run(self):
        # This is the code that will be run in a separate thread
        while True:  # Keep running the loop as long as the thread is alive
            # print("Thread - Solicitando dados para speeduino...")
            cmd = SPEEDUINO_CMD_A_CURR_STATUS
            data = self.speeduino.request_speeduino_data(cmd)
            # print(f"Dados recebidos: {data}")
            if data is not None:
                self.dataReceived.emit(data)  # Emit a signal with the received data
                self.speeduino.set_data_fields(data)
                self.speeduino.received_data = True
                # self.speeduino.printDeubgData()
            else:
                self.speeduino.received_data = False  # Atualiza o novo atributo
            time.sleep(self.speeduino.TIME_REQUEST_DATA)  # Pause between requests


class Speeduino:
    def __init__(self):
        self.port = ""
        self.last_request_time = time.time()  
        self.TIME_REQUEST_DATA = 0.4
        self.connection_status = False
        self.received_data = False

    def setFailedComm(self, msg):
        print(f"Falha na comunicacao: {msg}")
        self.connection_status = False
        self.received_data = False


    def connect(self, port):
        try:
            self.ser = serial.Serial(port, 115200, timeout=1)
            time.sleep(2)  # Aguarde 2 segundos para a conexão ser estabelecida
            
            # cmd = SPEEDUINO_CMD_A_CURR_STATUS
            self.connection_status = True
            if self.connection_status:
                # Se a conexão for bem-sucedida, inicie a thread
                self.request_thread = SpeeduinoRequestThread(self)
                self.request_thread.dataReceived.connect(self.set_data_fields)  # Conectar o sinal a um slot
                self.request_thread.start()  # Iniciar a thread
            else:
                logging.error("Failed to connect to Speeduino.")
            # data = self.request_speeduino_data(cmd)
            # if data is not None:
            #     self.set_data_fields(data)
            #     self.connection_status = True # "Conexão com a Speeduino estabelecida com sucesso."
            # else:
            #     logging.error("Failed to retrieve data from Speeduino.")
        except serial.SerialException as e:
            self.setFailedComm(f"Failed to open port {port}: {e}")
        except Exception as e:
            self.setFailedComm(e)

    # def __init__(self, port):
    #     self.last_request_time = time.time()  # adicione essa linha no __init__
    #     self.TIME_REQUEST_DATA = 0.5
    #     self.connection_status = False # "Falha na conexão com a Speeduino."
    #     self.received_data = False  # Status de dados recebidos da speeduino

    #     try:
    #         self.ser = serial.Serial(port, 115200, timeout=1)
    #         time.sleep(2)  # Aguarde 2 segundos para a conexão ser estabelecida
            
    #         # cmd = SPEEDUINO_CMD_A_CURR_STATUS
    #         self.connection_status = True
    #         if self.connection_status:
    #             # Se a conexão for bem-sucedida, inicie a thread
    #             self.request_thread = SpeeduinoRequestThread(self)
    #             self.request_thread.dataReceived.connect(self.set_data_fields)  # Conectar o sinal a um slot
    #             self.request_thread.start()  # Iniciar a thread
    #         else:
    #             logging.error("Failed to connect to Speeduino.")
    #         # data = self.request_speeduino_data(cmd)
    #         # if data is not None:
    #         #     self.set_data_fields(data)
    #         #     self.connection_status = True # "Conexão com a Speeduino estabelecida com sucesso."
    #         # else:
    #         #     logging.error("Failed to retrieve data from Speeduino.")
    #     except serial.SerialException as e:
    #         logging.error(f"Failed to open port {port}: {e}")
    #     except Exception as e:
    #         logging.error(f"An unexpected error occurred: {e}")

    def setTimeRequestData(self, newTime):
        self.TIME_REQUEST_DATA = newTime

    def getSpeduinoConnecStatus(self): 
        return self.connection_status

    def request_speeduino_data(self, cmd):
        try:
            current_time = time.time()
            if current_time - self.last_request_time >= self.TIME_REQUEST_DATA:
                self.ser.write(cmd[0].encode())
                self.last_request_time = current_time
                time.sleep(self.TIME_REQUEST_DATA)  # Aguarde antes de ler a resposta
                response = self.ser.read_all()
                if len(response) <= cmd[1]:
                    return None
                return response
        except serial.SerialTimeoutException as e:
            self.setFailedComm(f"Timeout occurred: {e}")
        except Exception as e:
            self.setFailedComm(f"An unexpected error occurred: {e}")

    def update(self):
        # Este método pode ser chamado para atualizar os dados da Speeduino
        cmd = SPEEDUINO_CMD_A_CURR_STATUS
        data = self.request_speeduino_data(cmd)
        if data is not None:
            self.set_data_fields(data)

    def close(self):
        self.ser.close()

    def printDeubgData(self):
        print("\r\r\r\n\n\nSPEEDUINO DATA: ")
        print("CNT: ", self.CNT)
        print("TPS: ", self.TPS)
        print("Battery Voltage: ", self.battery10)
        print("RPM: ", self.RPM)
        print("MAP: ", self.MAP)
        print("IAT: ", self.IAT)
        print("Coolant: ", self.coolant)

    def run(self):
        print("Esntou no run")
        try:
            while True:
                # self.update()

                # Agora você pode acessar os dados atualizados diretamente
                # das variáveis de instância de Speeduino.
                print("\r\r\r\n\n\nSPEEDUINO DATA: ")
                print("CNT: ", self.CNT)
                print("TPS: ", self.TPS)
                print("Battery Voltage: ", self.battery10)
                print("RPM: ", self.RPM)
                print("MAP: ", self.MAP)
                print("IAT: ", self.IAT)
                print("Coolant: ", self.coolant)

                # time.sleep(1)
        except KeyboardInterrupt:
            print("Program terminated.")
            self.close()
        except Exception as e:
            print("Error:", e)
            self.close()

    @staticmethod # pode ser chamado sem instanciar a Speeduino, para verificar em qual porta se conectar
    def list_ports():
        try:
            ports = serial.tools.list_ports.comports()
            available_ports = []
            print("Ports available:")
            for port in ports:
                print(port.device)
                available_ports.append(port.device)
            return available_ports
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return []

    def set_data_fields(self, data):
        self.CNT = data[0]
        self.status1 = data[1]
        self.engine = data[2]
        self.syncLossCounter = data[3]
        self.MAP = data[4] + (data[5] << 8)
        self.IAT = data[6]
        self.coolant = data[7]
        self.batCorrection = data[8]
        self.battery10 = data[9]
        self.O2 = data[10]
        self.egoCorrection = data[11]
        self.iatCorrection = data[12]
        self.wueCorrection = data[13]
        self.RPM = data[14] + (data[15] << 8)
        self.AEamount = data[16]
        self.corrections = data[17] + (data[18] << 8)
        self.VE1 = data[19]
        self.VE2 = data[20]
        self.afrTarget = data[21]
        self.tpsDOT = data[22]
        self.advance = data[23]
        self.TPS = data[24]
        self.loopsPerSecond = data[25] + (data[26] << 8)
        self.freeRAM = data[27] + (data[28] << 8)
        self.boostTarget = data[29]
        self.boostDuty = data[30]
        self.spark = data[31]
        self.rpmDOT = data[32] + (data[33] << 8)
        self.ethanolPct = data[34]
        self.flexCorrection = data[35]
        self.flexIgnCorrection = data[36]
        self.idleLoad = data[37]
        self.testOutputs = data[38]
        self.O2_2 = data[39]
        self.baro = data[40]
        self.canin = [data[i] + (data[i+1] << 8) for i in range(41, 73, 2)]
        self.tpsADC = data[73]
        self.nextError = data[74]
        self.PW = [data[i] + (data[i+1] << 8) for i in range(75, 83, 2)]
        self.status3 = data[83]
        self.engineProtectStatus = data[84]
        self.fuelLoad = data[85] + (data[86] << 8)
        self.ignLoad = data[87] + (data[88] << 8)
        self.dwell = data[89] + (data[90] << 8)
        self.CLIdleTarget = data[91]
        self.mapDOT = data[92]
        self.vvt1Angle = data[93] + (data[94] << 8)
        self.vvt1TargetAngle = data[95]
        self.vvt1Duty = data[96]
        self.flexBoostCorrection = data[97] + (data[98] << 8)
        self.baroCorrection = data[99]
        self.VE = data[100]
        self.ASEValue = data[101]
        self.vss = data[102] + (data[103] << 8)
        self.gear = data[104]
        self.fuelPressure = data[105]
        self.oilPressure = data[106]
        self.wmiPW = data[107]
        self.status4 = data[108]
        self.vvt2Angle = data[109] + (data[110] << 8)
        self.vvt2TargetAngle = data[111]
        self.vvt2Duty = data[112]
        self.outputsStatus = data[113]
        self.fuelTemp = data[114]
        self.fuelTempCorrection = data[115]
        self.advance1 = data[116]
        self.advance2 = data[117]
        self.TS_SD_Status = data[118]
        self.EMAP = data[119] + (data[120] << 8)
# def main():
#     print("Main")
#     Speeduino.list_ports()
#     port = 'COM24'
#     speeduino = Speeduino(port)
#     speeduino.run()

# if __name__ == "__main__":
#     main()