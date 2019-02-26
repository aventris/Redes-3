#!/usr/bin/env python

import rrdtool

def createTrafico(tiempo):
    ret = rrdtool.create("estadisticasTrafico.rrd",
                        "--start",tiempo,
                        "--step",'60',
                        "DS:InOctets:COUNTER:100:U:U",
                        "DS:OutOctets:COUNTER:100:U:U",
                        "RRA:AVERAGE:0.5:1:200")

    if ret:
        print (rrdtool.error())