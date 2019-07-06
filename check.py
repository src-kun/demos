#!/usr/bin/env python

import sys
import socket
import thread
import time

ports = []

def scan_port(port_num, host):
    s = socket.socket()
    socket.setdefaulttimeout(3)
    try:
        s.connect((host, port_num))
        ports.append(port_num)
    except Exception, e:
        pass

#host = 'localhost'
host = sys.argv[1]

for i in [22,8000,8080,3306,21,80,443]:
    try:
        scan_port(i, host)
    except:
        pass
print ports
