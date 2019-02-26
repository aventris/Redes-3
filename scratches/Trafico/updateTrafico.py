import time
import rrdtool
import sys
from getTrafico import consultaTrafico
from createTrafico import createTrafico
InOctets = 0
OutOctets = 0

contador = 0;
tiempoStart = str(int(time.time()))
createTrafico(tiempoStart)
while 1:
    InOctets = int(
        consultaTrafico('grupo4cm1','localhost',
                    '1.3.6.1.2.1.2.2.1.10.2')) #ifInOctets    1.3.6.1.2.1.4.20.1.2.192.168.0.16 = INTEGER: 2 --Para saber cual usar ipAdEntAddr en este caso 2
    OutOctets = int(
        consultaTrafico('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.2.2.1.16.2'))  # ifOutOctets


    valor = "N:" + str(InOctets) +':' +str(OutOctets)
    print (valor)
    rrdtool.update('estadisticasTrafico.rrd', valor)
    rrdtool.dump('estadisticasTrafico.rrd','estadisticasTrafico.xml')
    time.sleep(1)
    contador+=1
    if(contador == 10):
        print("**************")
        ret = rrdtool.graph("estadisticasTrafico.png",
                            "--start",tiempoStart,
                            "--end",'N',
                            "--vertical-label=Bytes/s",
                            "--width=700",
                            "--height=400",
                            "DEF:InOctets=estadisticasTrafico.rrd:InOctets:AVERAGE",
                            "DEF:OutOctets=estadisticasTrafico.rrd:OutOctets:AVERAGE",
                            "LINE2:InOctets#FF0000:InOctets",
                            "LINE2:OutOctets#00FF00:OutOctets\l")


        sys.stdout.flush()
        contador=0
