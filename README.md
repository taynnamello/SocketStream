# SocketStream


O software apresentado trata-se de um serviço de mensageria de rede, onde é possível a conexão de mais de um usuário a um servidor e as mensagens são armazenadas em arquivos txt.


## Bilbiotecas Utilizadas:


    - socket 
    - _thread
    - configparser 
    - datetime

## Versão

    Utilizar a versão 3.8 do Python

## Parâmetros Configuráveis cfg.ini

    IP do Servidor
    Porta
    Tamanho do Arquivo
    Time Out
    Prefixo dos arquivos de log


## Execução de Comandos

    1.1 Python server.py - Para subir o servidor onde a aplicação client.py irá se conectar

    1.2 Python client.py - Para conectar a aplicação e iniciar a troca de mensagens

É necessário que os comandos acima sejam executados em terminais separados para que tenha sucesso na conexão e troca de mensagens.

Ao executar a linha de comando Python server.py é exibida mensagem "Aguardando Conexão", até que o cliente informe IP do servidor que irá conectar

Ao executar a linha de comando Python client.py é exibida mensagem "Digite o IP de Conexão", após inserir o IP o cliente é conectado e inicia-se a troca de mensagens.

As mensagens trocadas são armazenadas em um arquivo txt por cliente conectado sem exceder o tamanho máximo definido no arquivo cfg.ini.

Ao exceder o tempo definido no arquivo cfg.ini(time_out) o cliente é desconectado por inatividade.

## Contato
Taynnã Mello da Silva

E-mail  - taynnamellosilva@gmail.com 

Linkedin - https://www.linkedin.com/in/taynnamellosilva/