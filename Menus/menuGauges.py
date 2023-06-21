# menuConnect.py
from PyQt6.QtWidgets import QMainWindow
from analoggaugewidget import *
from athenasUtils import *
from PyQt6.QtCore import QTimer
from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from analoggaugewidget import *
from athenasUtils import *

# Importar a classe Ui_MainWindow gerada do arquivo Python convertido
from ui_dashAthenas import *

class MenuGauges:
    def __init__(self, ui, speeduino, obd2):
        self.ui = ui
        self.myValue = 1
        self.toggleValue = 0
        self.speeduino = speeduino
        self.obd2 = obd2
        self.SPDConnected = False
        self.oldSDPConnectedStatus = False # controla o status da cor dos medidores

        # define as donfiguracoes de timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.autoUpdateValue)
        self.timer.start(50)  # Atualizar a cada 1000ms, ou 1 segundo

        # self.styleAnalogGaugeSpeed()
        self.initAnalogGaugeSpeed()
        self.initAnalogGaugeRPM()
        self.initAnalogGaugeCoolantTemp()
        self.initAnalogGaugeOilPressure()
        self.initAnalogGaugeFuel()
        self.initAnalogGaugeBattery()

        self.updateAllStyleAnalogGauge()

    def updateAllStyleAnalogGauge(self):
        self.styleAnalogGaugeSpeed(self.SPDConnected)
        self.styleAnalogGaugeCoolantTemp(self.SPDConnected)
        self.styleAnalogGaugeOilPressure(self.SPDConnected)
        self.styleAnalogGaugeFuel(self.SPDConnected)
        self.styleAnalogGaugeRPM(self.SPDConnected)
        self.styleAnalogGaugeBattery(self.SPDConnected)

    def styleAnalogGaugeSpeed(self, status):
        if status == False:
            self.ui.widgetSpeed.setGaugeTheme(4)
        else:
            self.ui.widgetSpeed.setOuterCircleColor(
                color1 = "#002523",
                color2 = "#990008",
                color3 = "#00F6E9"
            )

            self.ui.widgetSpeed.setCustomGaugeTheme(
                color1 = "#002523",
                color2 = "#990008",
                color3 = "#00F6E9"
            )
    
    def initAnalogGaugeSpeed(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False

        # Selecionar tema predefinido do medidor
        self.ui.widgetSpeed.setGaugeTheme(24)

        # Selecionar Montar um tema manualmente para o medidor
        self.ui.widgetSpeed.setCustomGaugeTheme(
            color1 = "#002523",
            color2 = "#990008",
            color3 = "#00F6E9"
        )


        # gradiente 
        #     color1 = "#e66465",  # primeira cor do gradiente CSS
        #     color2 = "#9198e5",  # segunda cor do gradiente CSS
        #     color3 = "#9198e5"   # repetindo a segunda cor para preencher o terceiro argumento

        # Gradiente Azul:
            # color1 = "#3c77e0",  # primeira cor do gradiente CSS
            # color2 = "#0c46b1",  # cor aproximadamente no meio do gradiente CSS
            # color3 = "#1a24eb"   # última cor do gradiente CSS

        # cores oficiais do tema 24    
        # color1="#009991",
        # color2="#080001",
        # color3="#FF0022"
        self.ui.widgetSpeed.setOuterCircleColor(
            color1 = "#002523",
            color2 = "#990008",
            color3 = "#00F6E9"
        )

        # seta a unidade de medida do Gauge:
        self.ui.widgetSpeed.units = " Km/h"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetSpeed.minValue = 0 
        self.ui.widgetSpeed.maxValue = 220
        self.ui.widgetSpeed.scalaCount = 12 

        # # Definir a posição inicial do ponteiro na escala
        # self.ui.widget.updateValue(int((self.ui.widget.maxValue - self.ui.widget.minValue) / 2))

        #  Definir ângulo de deslocamento das escalas do medidor
        # self.ui.widget.updateAngleOffset(0)

        # Definir ângulo inicial da escala
        # self.ui.widget.setScaleStartAngle(135)

        # Definir ângulo total da escala
        # self.ui.widget.setTotalScaleAngleSize(270)

        # Habilitar/Desabilitar gráfico de barras
        # barra lateral do grafico, se False, acompanha o ponteiro
        self.ui.widgetSpeed.setEnableBarGraph(False)

        # Habilitar/Desabilitar texto do valor
        # self.ui.widget.setEnableValueText(True)

        # Habilitar/Desabilitar ponto central
        # self.ui.widget.setEnableCenterPoint(True)

        # # Habilitar/Desabilitar ponteiro da agulha
        # self.ui.widget.setEnableNeedlePolygon(True)

        # # Habilitar/Desabilitar texto/numeracao da escala
        # self.ui.widget.setEnableScaleText(True)

        # # Habilitar/Desabilitar polígono da escala (Barra latera)
        # self.ui.widget.setEnableScalePolygon(True)

        # # Habilitar/Desabilitar grade de escala grande
        # self.ui.widget.setEnableBigScaleGrid(True)

        # # Habilitar/Desabilitar grade de escala fina
        # self.ui.widget.setEnableFineScaleGrid(True)

        # # Definir fator de raio externo da cor do medidor
        # self.ui.widget.setGaugeColorOuterRadiusFactor(1000)

        # # Definir fator de raio interno da cor do medidor
        self.ui.widgetSpeed.setGaugeColorInnerRadiusFactor(600)

        # Definir cor da agulha quando parada
        self.ui.widgetSpeed.setNeedleColor(R=255, G=0, B=0, Transparency=255)

        # # Definir cor da agulha ao arrastar
        # self.ui.widget.setNeedleColorOnDrag(R=0, G=0, B=255, Transparency=255)

        # Definir cor dos valores e numeros da escala
        self.ui.widgetSpeed.setScaleValueColor(R=255, G=255, B=255, Transparency=255)

        # # Definir cor do valor/unidades exibidos
        self.ui.widgetSpeed.setDisplayValueColor(R=255, G=255, B=255, Transparency=255) # branco
        # self.ui.widgetSpeed.setDisplayValueColor(R=0, G=153, B=145, Transparency=255) # azul tifane escura
        # self.ui.widgetSpeed.setDisplayValueColor(R=8, G=0, B=1, Transparency=255) # azul tifane pouco mais claro
        # self.ui.widgetSpeed.setDisplayValueColor(R=255, G=0, B=34, Transparency=255) # vermelho claro
        # self.ui.widgetSpeed.setDisplayValueColor(R=153, G=0, B=8, Transparency=255) # vermelho escuro
        # self.ui.widgetSpeed.setDisplayValueColor(R=0, G=246, B=233, Transparency=255) # tifani clarinho

        # color1 = (R=0, 153, 145, 255) # RGB equivalent of #009991
        # color2 = (R=8, 0, 1, 255) # RGB equivalent of #080001
        # color3 = (R=255, 0, 34, 255) # RGB equivalent of #FF0022
        # color4 = (R=0, 37, 35, 255) # RGB equivalent of #002523
        # color5 = (R=153, 0, 8, 255) # RGB equivalent of #990008
        # color6 = (R=0, 246, 233, 255) # RGB equivalent of #00F6E9



    def styleAnalogGaugeRPM(self, status):
        if status == False:
            self.ui.widgetRPM.setGaugeTheme(4)
        else:
            self.ui.widgetRPM.setGaugeTheme(24)

    def initAnalogGaugeRPM(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetRPM.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetRPM.units = " RPM"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetRPM.minValue = 0 
        self.ui.widgetRPM.maxValue = 8000
        self.ui.widgetRPM.scalaCount = 12

    def styleAnalogGaugeCoolantTemp(self, status):
        if status == False:
            self.ui.widgetCoolantTemp.setGaugeTheme(4)
        else:
            self.ui.widgetCoolantTemp.setGaugeTheme(24)

    def initAnalogGaugeCoolantTemp(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetCoolantTemp.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetCoolantTemp.units = " Temp"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetCoolantTemp.minValue = 0 
        self.ui.widgetCoolantTemp.maxValue = 125
        self.ui.widgetCoolantTemp.scalaCount = 12
    
    def styleAnalogGaugeOilPressure(self, status):
        if status == False:
            self.ui.widgetOilPressure.setGaugeTheme(4)
        else:
            self.ui.widgetOilPressure.setGaugeTheme(24)

    def initAnalogGaugeOilPressure(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetOilPressure.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetOilPressure.units = " Oil"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetOilPressure.minValue = 0 
        self.ui.widgetOilPressure.maxValue = 100
        self.ui.widgetOilPressure.scalaCount = 12

    def styleAnalogGaugeFuel(self, status):
        if status == False:
            self.ui.widgetFuel.setGaugeTheme(4)
        else:
            self.ui.widgetFuel.setGaugeTheme(24)

    def initAnalogGaugeFuel(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetFuel.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetFuel.units = " Fuel"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetFuel.minValue = 0 
        self.ui.widgetFuel.maxValue = 100
        self.ui.widgetFuel.scalaCount = 10

    def styleAnalogGaugeBattery(self, status):
        if status == False:
            self.ui.widgetBattery.setGaugeTheme(4)
        else:
            self.ui.widgetBattery.setGaugeTheme(24)

    def initAnalogGaugeBattery(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetBattery.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetBattery.units = " Volt"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetBattery.minValue = 0 
        self.ui.widgetBattery.maxValue = 20
        self.ui.widgetBattery.scalaCount = 12

    def testMode(self):
        minCntValue = 0
        maxCntValue = 300
        
        # if self.currentPage == 3:
        # Aqui você atualizaria o valor que você quer mostrar no medidor.
        # Por exemplo, vamos apenas incrementar o valor atual.
        # print(f"Ola: {self.myValue}")
        if self.toggleValue == 0:
            self.myValue += 1  # Isso fará com que o widget seja redesenhado
        else: 
            self.myValue -= 1

        if self.myValue > maxCntValue:
            self.toggleValue = 1
        elif self.myValue <= 1:
            self.toggleValue = 0

        self.ui.widgetRPM.updateValue(map_value(self.myValue, minCntValue, maxCntValue, self.ui.widgetRPM.minValue, self.ui.widgetRPM.maxValue))
        self.ui.widgetSpeed.updateValue(self.myValue)
        self.ui.widgetOilPressure.updateValue(self.myValue)
        self.ui.widgetFuel.updateValue(self.myValue)
        self.ui.widgetCoolantTemp.updateValue(map_value(self.myValue, minCntValue, maxCntValue, self.ui.widgetCoolantTemp.minValue, self.ui.widgetCoolantTemp.maxValue))
        self.ui.widgetBattery.updateValue(self.myValue)

    def autoUpdateValue(self):

        testeMode = False # habilita o modo de teste dos gauges
        if testeMode == True:
            self.testMode()
            return

        # OBD2
        if (self.obd2.connection_status == True & self.obd2.received_data == True):
            self.SPDConnected = True
            
            self.ui.widgetSpeed.updateValue(self.obd2.SPEED)
            self.ui.widgetRPM.updateValue(self.obd2.RPM)
            self.ui.widgetOilPressure.updateValue(self.obd2.OIL_PRESSURE)
            self.ui.widgetFuel.updateValue(self.obd2.FUEL_LEVEL)
            self.ui.widgetCoolantTemp.updateValue(self.obd2.COOLANT_TEMP)
            self.ui.widgetBattery.updateValue(self.obd2.BATTERY)
            self.updateAllStyleAnalogGauge()
        else:
            self.SDPConnected = False
            self.ui.widgetSpeed.updateValue(0)
            self.ui.widgetRPM.updateValue(0)
            self.ui.widgetOilPressure.updateValue(0)
            self.ui.widgetFuel.updateValue(0)
            self.ui.widgetCoolantTemp.updateValue(0)
            self.ui.widgetBattery.updateValue(0)
            self.updateAllStyleAnalogGauge()

        # Speeduino
        # if (self.speeduino.connection_status == True & self.speeduino.received_data == True):
        #     self.SPDConnected = True

        #     self.ui.widgetSpeed.updateValue(self.speeduino.CNT)
        #     self.ui.widgetRPM.updateValue(self.speeduino.battery10)
        #     self.ui.widgetOilPressure.updateValue(0)
        #     self.ui.widgetFuel.updateValue(0)
        #     self.ui.CoolantTemp.updateValue(0)
        #     self.ui.widgetBattery.updateValue(0)
        #     self.updateAllStyleAnalogGauge()
        # else:
        #     self.SDPConnected = False
        #     self.ui.widgetSpeed.updateValue(0)
        #     self.ui.widgetRPM.updateValue(0)
        #     self.ui.widgetOilPressure.updateValue(0)
        #     self.ui.widgetFuel.updateValue(0)
        #     self.ui.CoolantTemp.updateValue(0)
        #     self.ui.widgetBattery.updateValue(0)
        #     self.updateAllStyleAnalogGauge()

        # if self.oldSDPConnectedStatus != self.SDPConnected:
            
        #     self.oldSDPConnectedStatus = self.SDPConnected

        # self.ui.widgetRPM.updateValue(map_value(self.myValue, minCntValue, maxCntValue, self.ui.widgetRPM.minValue, self.ui.widgetRPM.maxValue))
        # 
        # self.ui.widgetOilPressure.updateValue(self.myValue)
        # self.ui.widgetFuel.updateValue(self.myValue)
        # self.ui.CoolantTemp.updateValue(map_value(self.myValue, minCntValue, maxCntValue, self.ui.CoolantTemp.minValue, self.ui.CoolantTemp.maxValue))
        # self.ui.widgetBattery.updateValue(self.myValue)