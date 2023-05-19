from speeduino import *

# def main():
#     print("Main")
#     Speeduino.list_ports()
#     port = 'COM24'
#     speeduino = Speeduino(port)

#     while True:
#         try:
#             speeduino.update()

#             # Agora você pode acessar os dados atualizados diretamente
#             # das variáveis de instância de Speeduino.
#             print("\r\r\r\n\n\nSPEEDUINO DATA: ")
#             print("CNT: ", speeduino.CNT)
#             print("TPS: ", speeduino.TPS)
#             print("Battery Voltage: ", speeduino.battery10)
#             print("RPM: ", speeduino.RPM)
#             print("MAP: ", speeduino.MAP)
#             print("IAT: ", speeduino.IAT)
#             print("Coolant: ", speeduino.coolant)

#             time.sleep(1)
#         except KeyboardInterrupt:
#             print("Program terminated.")
#             speeduino.ser.close()
#             break
#         except Exception as e:
#             print("Error:", e)
#             speeduino.ser.close()
#             break

# if __name__ == "__main__":
#     main()









# class Speeduino:
#     # Restante do código omitido para brevidade...



def main():
    print("Main")
    Speeduino.list_ports()
    port = 'COM24'
    speeduino = Speeduino(port)
    speeduino.run()

if __name__ == "__main__":
    main()