import socket 
import _thread
import configparser
import datetime

def carregaConfiguracoes():
    config = configparser.ConfigParser()
    config.read('cfg.ini')    
    return config

#Cria objeto de parser do ini
config = carregaConfiguracoes

def montarTextoMensagem(msg):
    return datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ' : ' + msg.decode("utf-8")

def testarSeExcedeuTamanho(arquivo, msg):
    tamanhoMsg = len(montarTextoMensagem(msg))
    return (arquivo.tell() + tamanhoMsg) > int(config['DEFAULT']['tamanho_arquivo'])

def gerarNovoArquivoLog(cliente):
    nomeArq = config['DEFAULT']['prefixo'] +  datetime.datetime.now().strftime('%Y%m%d%H%M%S') + ' - ' + cliente[0] + ' - ' + str(cliente[1]) + '.txt'
    return open("log/" + nomeArq, 'w')    

def conexaoCliente(con, cliente):
    try:
        print("Conectado por", cliente)
        arquivoGerado = False
        
        while True:
            msg = con.recv(1024)
            if not msg: 
                break
            
            #Entra na primeira execução para gerar o primeiro arquivo ou quando exceder o tamanho configurado
            if not arquivoGerado or testarSeExcedeuTamanho(arquivo, msg):            
                arquivo.close()
                arquivo = gerarNovoArquivoLog(cliente) 
                arquivoGerado = True  

            arquivo.write(montarTextoMensagem(msg) + '\n')  
            print(cliente, msg.decode("utf-8"))        

        print("Finalizando conexao do cliente", cliente)
        con.close()
        _thread.exit()
    except:
        print("Cliente desconectado por inatividade", cliente)
        con.close()
        _thread.exit()

host = config['DEFAULT']['ip']
port = config['DEFAULT']['porta']

addr = (host, int(port)) 
#sobe o servidor socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
server.bind(addr) 
server.listen(10) 

print("Aguardando conexões!")

while True:
    #Aguarda conexao do cliente
    con, cliente = server.accept()
    #Seta time out do ini
    con.settimeout(int(config['DEFAULT']['time_out']))
    _thread.start_new_thread(conexaoCliente, tuple([con, cliente]))
