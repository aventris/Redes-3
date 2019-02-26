#!/usr/bin/env python

import rrdtool

def createIP(tiempo):
    ret = rrdtool.create("estadisticasIP.rrd",
                        "--start",tiempo,
                        "--step",'60',
                        "DS:InReceives:COUNTER:100:U:U",
                        "DS:OutTransmits:COUNTER:100:U:U",
                        "DS:InDelivers:COUNTER:100:U:U",
                        "DS:OutRequests:COUNTER:100:U:U",
                        "DS:InOctets:COUNTER:100:U:U",
                        "DS:OutOctets:COUNTER:100:U:U",
                        "RRA:AVERAGE:0.5:1:200")

    if ret:
        print (rrdtool.error())