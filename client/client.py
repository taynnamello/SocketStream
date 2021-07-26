import socket 

ip = input("digite o ip de conexao: ") 
port = 7000 
addr = ((ip,port)) 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client_socket.connect(addr) 
print("Para sair use CTRL+C\n")
msg = input()
while str.encode(msg) != '\x18':
    try:
        client_socket.send(str.encode(msg)) 
        msg = input()
    except:
        print("Desconectado por inatividade")
        break

client_socket.close()