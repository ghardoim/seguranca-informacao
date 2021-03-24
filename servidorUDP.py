import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Socket criado com sucesso!")

host = "localhost"
porta = 5432
mensagem = "Olá, mundo!"

soc.bind((host, porta))

while 1:
  dados, end = soc.recvfrom(4096)

  if dados:
    print("Servidor enviando mensagem!")
    soc.sendto(dados + "\nServidor: ".encode() + mensagem.encode(), end)
