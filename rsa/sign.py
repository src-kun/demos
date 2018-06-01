#!/usr/bin/python
#coding=utf-8

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import MD5
from Crypto import Random

# 伪随机数生成器
random_generator = Random.new().read

# 生成2048比特秘钥对(pk, sk)
rsa = RSA.generate(2048, random_generator)
private_pem = rsa.exportKey()
with open('master-privatekey.pem', 'w') as f:
	f.write(private_pem)
public_pem = rsa.publickey().exportKey()
with open('master-publickey.pem', 'w') as f:
	f.write(public_pem)

message = '{"date":"Fri Jun  1 04:04:23 EDT 2018", "md5":"2d7aa5d9dbb7bad9774fd8df5e544838", "last":"v1", "sign":""}'

# 对消息进行签名
h = MD5.new(message)
private_key = RSA.importKey(open('master-privatekey.pem').read())
signer = PKCS1_v1_5.new(private_key)
signature = signer.sign(h)

# 对消息进行签名验证
h = MD5.new(message)
public_key = RSA.importKey(open('master-publickey.pem', 'r').read())
verifier = PKCS1_v1_5.new(public_key)
if verifier.verify(h, signature):
	print "OK"
else:
	print "Invalid Signature"