#!/usr/bin/env python

import sys
import socket

def scan_port(port_num, host):
    s = socket.socket()
    socket.setdefaulttimeout(2)
    try:
        s = s.connect((host, port_num))
        print port_num, "[+] connection successful"

    except Exception, e:
        pass

#host = 'localhost'
host =sys.argv[1]

for i in xrange(65535):
    scan_port(i, host)
