# menuConnect.py
from PyQt5.QtWidgets import QMainWindow
from analoggaugewidget import *
from athenasUtils import *
from PyQt5.QtCore import QTimer
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from analoggaugewidget import *
from athenasUtils import *

# Importar a classe Ui_MainWindow gerada do arquivo Python convertido
from ui_dashAthenas import *

class MenuGauges:
    def __init__(self, ui):
        self.ui = ui
        self.myValue = 1
        self.toggleValue = 0

        # define as donfiguracoes de timer:
        self.timer = QTimer()
        self.timer.timeout.connect(self.autoUpdateValue)
        self.timer.start(50)  # Atualizar a cada 1000ms, ou 1 segundo

        self.styleAnalogGaugeSpeed()
        self.styleAnalogGaugeRPM()
        self.styleAnalogGaugeDuty()
        self.styleAnalogGaugeMAP()
        self.styleAnalogGaugePW()
        self.styleAnalogGaugeTPS()

    def styleAnalogGaugeSpeed(self):
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
        self.ui.widgetSpeed.maxValue = 300
        self.ui.widgetSpeed.scalaCount = 15 

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




    def styleAnalogGaugeRPM(self):
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
        self.ui.widgetRPM.maxValue = 12
        self.ui.widgetRPM.scalaCount = 12

    def styleAnalogGaugeTPS(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetTPS.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetTPS.units = " TPS"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetTPS.minValue = 0 
        self.ui.widgetTPS.maxValue = 100
        self.ui.widgetTPS.scalaCount = 10

    def styleAnalogGaugeDuty(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetDuty.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetDuty.units = " Duty"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetDuty.minValue = 0 
        self.ui.widgetDuty.maxValue = 300
        self.ui.widgetDuty.scalaCount = 15

    def styleAnalogGaugePW(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetPW.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetPW.units = " PW"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetPW.minValue = 0 
        self.ui.widgetPW.maxValue = 300
        self.ui.widgetPW.scalaCount = 15

    def styleAnalogGaugeMAP(self):
        # *********************************************
        # customizar os medidores:
        # *********************************************
        # aqui controla a barra de velocidade
        # self.ui.widget.enableBarGraph = False


        # Selecionar tema predefinido do medidor
        self.ui.widgetMAP.setGaugeTheme(24)

        # seta a unidade de medida do Gauge:
        self.ui.widgetMAP.units = " Engine\nMAP"
        # self.ui.widgetRpm.value_fontname = "DS-Digital"

        # seta o valor valores de escala do Gauge:
        self.ui.widgetMAP.minValue = 0 
        self.ui.widgetMAP.maxValue = 300
        self.ui.widgetMAP.scalaCount = 15

    def autoUpdateValue(self):

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
        self.ui.widgetDuty.updateValue(self.myValue)
        self.ui.widgetPW.updateValue(self.myValue)
        self.ui.widgetTPS.updateValue(map_value(self.myValue, minCntValue, maxCntValue, self.ui.widgetTPS.minValue, self.ui.widgetTPS.maxValue))
        self.ui.widgetMAP.updateValue(self.myValue)