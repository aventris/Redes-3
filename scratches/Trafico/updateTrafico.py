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
        consultaTrafico('variation/virtualtable','10.100.71.200',
                    '1.3.6.1.2.1.2.2.1.12.1'))
    valor = "N:"+str(InOctets)
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
                            "LINE2:InOctets#FF0000:InOctets",)


        sys.stdout.flush()
        contador=0
