#!/usr/bin/python
# -*- coding: utf-8 -*- 
"""
利用卡巴斯基检测木马
"""

import os

os.system('cd C:\\Program Files (x86)\\Kaspersky Lab\\Kaspersky Total Security 18.0.0 && avp.com scan "C:\\Users\\max\\Desktop\\scan" > C:\\Users\\max\\Desktop\\scan\\1.txt')
#TODO 找出卡巴斯基所有病毒类型
avp_type = ['Trojan']
file_names = ['444.exe', 'app.exe', 'a_v6.exe', 'avp.py', 'builder.exe', 'builder.exe.1', 'crtptdsteve.exe', 'data.xls', 'desktopbin.exe', 'dll_rewiew.exe', 'erufudjjsnaweq.exe', 'fedex.bin', 'getfile.bin', 'hello.bin', 'hhueiqpii.exe', 'igrmwns.exe', 'index.html', 'index.html.1', 'index.html.2', 'index.html.3', 'index.html.4', 'index.html.5', 'index.html.6', 'Invoice.exe', 'iwantapple.exe', 'java.exe', 'k815gBU', 'lakhost.exe', 'lel.exe', 'loder.exe', 'log.txt', 'Loki_original.exe', 'Loki_original.exe.1', 'merv1.exe', 'm.exe', 'm.rar', 'nds.exe', 'obo.exe', '_output153DF00.exe', '_output1E66A80.exe', 'outurg.bin', 'putty.exe', 'quakes.exe', 'r24.exe', 'read.txt', 'rules.txt', 'soperos.bin', 'start.exe', 'steve.exe', 'Stt.exe', 'timedllx.exe', 'trojan.zip', '中控渗透测试.docx', 'mimikatz.exe']
fop = open('C:\\Users\\max\\Desktop\\scan\\1.txt')
try:
	text = fop.read( )
finally:
	fop.close()

#解析结果
def analysis_result(result, file_names):
	info = {}
	for name in file_names:
		for res in result:
			if name in res:
				if not info.has_key(name):
					info[name] = []
				info[name].append(res)
	return info
info = analysis_result(text.split('\n'), file_names)
#print trojans
#找出木马文件
for name in info:
	for res in info[name]:
		for type in avp_type:
			if type in res:
				print res
				print name













