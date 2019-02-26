import time
import rrdtool
import sys
from getICMP import consultaICMP
from createICMP import createICMP
InMsgs = 0
InErrors = 0
OutMsgs = 0
OutErrors = 0

contador = 0;
tiempoStart = str(int(time.time()))
createICMP(tiempoStart)
while 1:
    InMsgs = int(
        consultaICMP('grupo4cm1','localhost',
                    '1.3.6.1.2.1.5.29.1.2.1')) #ipSystemStatsInRecieves
    InErrors = int(
        consultaICMP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.5.29.1.3.1'))  # ipSystemStatsOutTransmits
    OutMsgs = int(
        consultaICMP('grupo4cm1', 'localhost',
                    '1.3.6.1.2.1.5.29.1.4.1'))  # ipSystemStatsInDelivers
    OutErrors = int(
        consultaICMP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.5.29.1.5.1'))  # ipSystemStatsOutRequests

    valor = "N:" + str(InMsgs) +':' +str(InErrors)+ ':' + str(OutMsgs) + ':' + str(OutErrors)
    print (valor)
    rrdtool.update('estadisticasICMP.rrd', valor)
    rrdtool.dump('estadisticasICMP.rrd','estadisticasICMP.xml')
    time.sleep(1)
    contador+=1
    if(contador == 10):
        print("**************")
        ret = rrdtool.graph("estadisticasICMP.png",
                            "--start",tiempoStart,
                            "--end",'N',
                            "--vertical-label=Bytes/s",
                            "--width=700",
                            "--height=400",
                            "DEF:InMsgs=estadisticasICMP.rrd:InMsgs:AVERAGE",
                            "DEF:InErrors=estadisticasICMP.rrd:InErrors:AVERAGE",
                            "DEF:OutMsgs=estadisticasICMP.rrd:OutMsgs:AVERAGE",
                            "DEF:OutErrors=estadisticasICMP.rrd:OutErrors:AVERAGE",
                            "LINE2:InMsgs#FF0000:InMsgs",
                            "LINE2:InErrors#00FF00:InErrors\l",
                            "LINE2:OutMsgs#0000FF:OutMsgs",
                            "LINE2:OutErrors#FF00FF:OutErrors\l")


        sys.stdout.flush()
        contador=0
