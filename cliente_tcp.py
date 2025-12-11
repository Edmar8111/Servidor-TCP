import socket  # Biblioteca para conexões de rede
from decouple import config

class AcessarServer:
    def __init__(self, host=config("HOST", default="127.0.0.1", cast=str), port=config("PORT", default=5000, cast=int)):
        # Cria o cliente TCP
        self.host=host
        self.port=port
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def sendobj(self, obj):
        # Endereço e porta do servidor (devem ser iguais aos do servidor)
        # conecta ao servidor
        self.cliente.connect((self.host, self.port))
        print("Conectado ao servidor!")
        
        # Envia a mensagem
        mensagem = '{"a":0}'
        data=str(obj).encode('utf-8')
        
        self.cliente.send(data)

        # Recebe a resposta do servidor
        resposta = self.cliente.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {resposta}")

        # Fecha a conexão
        self. cliente.close()
        print("Conexão encerrada.")

if __name__=="__main__":
    AcessarServer().sendobj({"Teste":0})