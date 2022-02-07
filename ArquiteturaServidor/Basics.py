import socket
import time
import argparse
from typing import Any


class Args:
    @staticmethod
    def command_line(choice):
        """Analise a linha de comando e retorna endereços para o socket"""
        parser = argparse.ArgumentParser(description="Um cliente e servidor simples com interface de linha de comando")
        parser.add_argument("lado", choices=choice, help="Escolhe o servidor ou cliente", metavar="servidor/cliente")
        parser.add_argument('--o', "--internetProtocol", help="Insira o ip", metavar="Host",
                            required=False, default='127.0.0.1')
        parser.add_argument("--p", "--port", help="Insira a porta de comunicação do serviço",
                            metavar="Port", default="7777", type=int)
        args = parser.parse_args()
        function = choice[args.lado]
        return function((args.o, args.p))


class Serv:
    """Servidor TCP, constroi e escuta um socket"""

    @staticmethod
    def listen(addr):
        host, port = addr
        print(addr)
        soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soquete.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        soquete.bind((host, port))
        soquete.listen(64)
        print(f"Listen at {host}:{port}...")
        """Sempre vai responder às conexões recebidas no soquete de escuta"""
        while True:
            new_sock, addr = soquete.accept()  # addr endereco do cliente, new soque, cuida dos envios de msg,
            # enquanto o outro so firma a conexão
            print(f"Receiving connection from {addr}")
            try:
                while True:
                    # msg recebida
                    msg = new_sock.recv(4096)
                    if not msg:
                        raise EOFError("Socket closed!")
                    else:
                        time.sleep(0.001)
                        print(f"{addr} said: {msg.decode()}")
                        new_sock.sendall("[*] Received!".encode())
            except EOFError:
                print(f"Client socket, {addr} has closed!")
            except Exception as e:
                print(e)
            finally:
                new_sock.close()


class Client:
    @staticmethod
    def request(addr):
        """Cliente que conecta ao endereço do servidor"""
        serv_addr = addr
        soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soquete.connect(serv_addr)
        soquete.sendall("client: Client connecting at serv...".encode())
        print(f"the serv said: {soquete.recv(4096).decode()}")


if __name__ == '__main__':
    choices = {
       "servidor": Serv.listen,
       "cliente": Client.request,
    }
    Args.command_line(choices)

