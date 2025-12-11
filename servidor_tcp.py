import socket  # Biblioteca que permite criar conexões de rede
import json
from decouple import config


# Server TCP
ativo=0
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET → IPv4 # SOCK_STREAM → indica o protocolo TCP

# Ligamos o servidor ao endereço e porta
servidor.bind((config("HOST",default='127.0.0.1',cast=str), config("PORT", default=5000, cast=int))) # Definimos o endereço e a porta do servidor
print("Servidor Ativado")

# Aguarda conexões

while ativo!=None:
    ativo=1
    servidor.listen()

    # Recebe a requisição de conexão do cliente
    conexao, endereco = servidor.accept()
    print(f"Cliente conectado: {endereco}")

    dados = conexao.recv(1024).decode("utf-8") # Definimos o máximo 1024 bytes por mensagem
    
    #Bloco que efetua a conversão dos dados para um dicionario
    try:
        dados=json.loads(dados)
        print(f"Payload Recebida -> {dados}")
    except:
        try:
            dados=eval(dados)
            print(f"Payload Recebida -> {dados}")
        except Exception as e: 
            ativo=None
            print(f"Error -> {e}")

    # Retorno ao cliente
    resposta = "Servidor recebeu sua mensagem com sucesso!"
    conexao.send(resposta.encode('utf-8'))

# Fecha a conexão
conexao.close()
servidor.close()
print("Conexão encerrada.")
