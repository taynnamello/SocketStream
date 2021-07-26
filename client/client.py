import socket 

ip = input("digite o ip de conexao: ") 
port = input("digite a porta para conexao: ") 

addr = ((ip,int(port))) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
print("Para sair use CTRL+C\n")
msg = input()
while True:
    try:
        client_socket.send(str.encode(msg)) 
        msg = input()
    except:
        print("Desconectado por inatividade")
        break

client_socket.close()