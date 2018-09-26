#!/usr/bin/python
#coding:utf-8 
import smtplib
import imaplib
import email
from email.MIMEText import MIMEText
from email.Utils import formatdate
from email.Header import Header
import sys
import os

#设置默认字符集为UTF8 不然有些时候转码会出问题
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)

#发送邮件的相关信息，根据你实际情况填写
smtp_host = 'smtp.exmail.qq.com'
#smtp_port = '25'
ssl_port= '465'
imap_host = 'imap.exmail.qq.com'
imap_port = '993'

fromMail = 'test@xx.com'
toMail = 'xxx@xx.com'
username = 'test@xx.com'
password = '123456'

#subject 邮件标题
#body 内容
def send(subject, body):
	#初始化邮件
	encoding = 'utf-8'
	mail = MIMEText(body.encode(encoding),'plain',encoding)
	mail['Subject'] = Header(subject,encoding)
	mail['From'] = fromMail
	mail['To'] = toMail
	mail['Date'] = formatdate()
	try:
		#连接smtp服务器，明文/SSL/TLS三种方式，根据你使用的SMTP支持情况选择一种
		#普通方式，通信过程不加密
		#smtp = smtplib.SMTP(smtp_host,smtp_port)
		#smtp.ehlo()
		#smtp.login(username,password)

		#tls加密方式，通信过程加密，邮件数据安全，使用正常的smtp端口
		#smtp = smtplib.SMTP(smtp_host,smtp_port)
		#smtp.set_debuglevel(True)
		#smtp.ehlo()
		#smtp.starttls()
		#smtp.ehlo()
		#smtp.login(username,password)

		#纯粹的ssl加密方式，通信过程加密，邮件数据安全
		smtp = smtplib.SMTP_SSL(smtp_host,ssl_port)
		smtp.set_debuglevel(True)
		smtp.ehlo()
		smtp.login(username,password)

		#发送邮件
		smtp.sendmail(fromMail,toMail,mail.as_string())
		smtp.close()
	except Exception as e:
		print e

def receive():
	imap = imaplib.IMAP4_SSL(port = imap_port, host = imap_host)
	imap.login(username, password)
	#选择一个邮件文件夹，默认为INBOX
	imap.select()

	#获取未读邮件
	unseen = imap.search(None, 'UnSeen')
	unread_id = unseen[1][0].split()
	for id in  unread_id:
		type, data = imap.fetch(id, 'RFC822')
		content = data[0][1]
		msg = email.message_from_string(content)
		for part in msg.walk():
			if part.is_multipart():
				continue
			if part.get('Content-Disposition') is None:
				continue
			file_data = part.get_payload(decode = True)
			filename = email.Header.decode_header(part.get_filename())[0][0]
			download_path = os.path.join('/tmp/', filename)
			with open(download_path, 'wb') as fp:
				fp.write(file_data)
	imap.close()
	imap.logout()
	#https://zhuanlan.zhihu.com/p/28377718

subject = u'[Notice]hello'
body = u'hello,this is a mail from ' + fromMail
send(subject, body)
receive()