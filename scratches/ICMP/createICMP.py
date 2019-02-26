#!/usr/bin/env python

import rrdtool

def createICMP(tiempo):
    ret = rrdtool.create("estadisticasICMP.rrd",
                        "--start",tiempo,
                        "--step",'60',
                        "DS:InMsgs:COUNTER:100:U:U",
                        "DS:InErrors:COUNTER:100:U:U",
                        "DS:OutMsgs:COUNTER:100:U:U",
                        "DS:OutErrors:COUNTER:100:U:U",
                        "RRA:AVERAGE:0.5:1:200")

    if ret:
        print (rrdtool.error())