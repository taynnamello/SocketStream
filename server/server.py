import socket 
import _thread
import configparser
import datetime

config = configparser.ConfigParser()
config.read('cfg.ini')

host = config['DEFAULT']['ip']
port = config['DEFAULT']['porta']

addr = (host, int(port)) 
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
serv_socket.bind(addr) 
serv_socket.listen(10) 

print("Aguardando conexão!")

def gerarArquivo(cliente):
    nomeArq = config['DEFAULT']['prefixo'] +  datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ' - ' + cliente[0] + ' - ' + str(cliente[1]) + '.txt'
    return open("log/" + nomeArq, 'w')    

def conectado(con, cliente):
    try:
        print("Conectado por", cliente)
        arquivoGerado = False
        
        while True:
            msg = con.recv(1024)
            if not msg: 
                break
            
            if not arquivoGerado:
               arquivo = gerarArquivo(cliente) 
               arquivoGerado = True
        
            tamanhoMsg = len(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ' : ' + msg.decode("utf-8"))
        
            if (arquivo.tell() + tamanhoMsg) > int(config['DEFAULT']['tamanho_arquivo']):
                arquivo.close()
                arquivo = gerarArquivo(cliente)   

            arquivo.write(datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ' : ' + msg.decode("utf-8") + '\n')  
            print(cliente, msg.decode("utf-8"))        

        print("Finalizando conexao do cliente", cliente)
        con.close()
        _thread.exit()
    except:
        print("Cliente desconectado por inatividade", cliente)
        con.close()
        _thread.exit()

while True:
    con, cliente = serv_socket.accept()
    con.settimeout(int(config['DEFAULT']['time_out']))
    _thread.start_new_thread(conectado, tuple([con, cliente]))
