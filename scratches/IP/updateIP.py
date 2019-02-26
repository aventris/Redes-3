import time
import rrdtool
import sys
from getIP import consultaIP
from createIP import createIP
InReceives = 0
OutTransmits = 0
OutOctets = 0
OutRequests = 0
InDelivers = 0
InOctets = 0

contador = 0;
tiempoStart = str(int(time.time()))
createIP(tiempoStart)
while 1:
    InReceives = int(
        consultaIP('grupo4cm1','localhost',
                    '1.3.6.1.2.1.4.31.1.1.3.1')) #ipSystemStatsInRecieves
    OutTransmits = int(
        consultaIP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.4.31.1.1.30.1'))  # ipSystemStatsOutTransmits
    InDelivers = int(
        consultaIP('grupo4cm1', 'localhost',
                    '1.3.6.1.2.1.4.31.1.1.18.1'))  # ipSystemStatsInDelivers
    OutRequests = int(
        consultaIP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.4.31.1.1.20.1'))  # ipSystemStatsOutRequests
    InOctets = int(
        consultaIP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.4.31.1.1.5.1'))  # ipSystemStatsInOctets
    OutOctets = int(
        consultaIP('grupo4cm1', 'localhost',
                   '1.3.6.1.2.1.4.31.1.1.32.1'))  # ipSystemStatsOutOctets

    valor = "N:" + str(InReceives) +':' +str(OutTransmits)+ ':' + str(InDelivers) + ':' + str(OutRequests) + ':' + str(InOctets) + ':' + str(OutOctets)
    print (valor)
    rrdtool.update('estadisticasIP.rrd', valor)
    rrdtool.dump('estadisticasIP.rrd','estadisticasIP.xml')
    time.sleep(1)
    contador+=1
    if(contador == 10):
        print("**************")
        ret = rrdtool.graph("traficoIP.png",
                            "--start",tiempoStart,
                            "--end",'N',
                            "--vertical-label=Bytes/s",
                            "--width=700",
                            "--height=400",
                            "DEF:InReceives=estadisticasIP.rrd:InReceives:AVERAGE",
                            "DEF:OutTransmits=estadisticasIP.rrd:OutTransmits:AVERAGE",
                            "DEF:InDelivers=estadisticasIP.rrd:InDelivers:AVERAGE",
                            "DEF:OutRequests=estadisticasIP.rrd:OutRequests:AVERAGE",
                            "LINE2:InReceives#FF0000:InReceives",
                            "LINE1:OutTransmits#00FF00:OutTransmits\l",
                            "LINE1:InDelivers#0000FF:InDelivers",
                            "LINE1:OutRequests#FF00FF:OutRequests\l")

        ret = rrdtool.graph("trafico-OctetosIP.png",
                            "--start", tiempoStart,
                            "--end", 'N',
                            "--vertical-label=Bytes/s",
                            "--width=700",
                            "--height=400",
                            "DEF:InOctets=estadisticasIP.rrd:InOctets:AVERAGE",
                            "DEF:OutOctets=estadisticasIP.rrd:OutOctets:AVERAGE",
                            "LINE2:InOctets#FF0000:InOctets",
                            "LINE1:OutOctets#00FF00:OutOctets\l")
        sys.stdout.flush()
        contador=0
