import sys
import rrdtool
import time
tiempo_actual = int(time.time())
tiempo_final = tiempo_actual - 86400
tiempo_inicial = tiempo_final -25920000

for x in range(0,1):
    ret = rrdtool.graph( "estadisticasICMP.png",
                     "--start",'1550953560',
                     "--end","1550953860",
                     "--vertical-label=Bytes/s",
                     "DEF:inoctets=estadisticasIP.rrd:inReceives:AVERAGE",
                     "DEF:outoctets=estadisticasIP.rrd:InOctets:AVERAGE",
                     "AREA:InOctets#00FF00:In traffic",
                     "LINE1:outoctets#0000FF:Out traffic\r")

    time.sleep(30)