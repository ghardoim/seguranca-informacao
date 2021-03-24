import socket
import sys

def main():
  try:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
  
  except socket.error as erro:
    print("A conexão falhou!")
    print(f"Erro: {erro}")
    sys.exit()

  print(f"Socket criado com sucesso")

  host_alvo = input("Digite o host ou ip a ser conectado: ")
  porta_alvo = int(input("Digite a porta a ser conectada: "))

  try:
    soc.connect((host_alvo, porta_alvo))
    print(f"Cliente tcp conectado com sucesso em {host_alvo}:{porta_alvo}")
    soc.shutdown(2)

  except socket.error as erro:
    print(f"Não foi possível conectar em {host_alvo}:{porta_alvo}")
    print(f"Erro: {erro}")
    sys.exit()

if "__main__" == __name__:
  main()