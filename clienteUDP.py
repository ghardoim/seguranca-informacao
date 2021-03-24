import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente socket criado com sucesso!")

host = "localhost"
porta = 5432
mensagem = "Olá, mundo!"

try:
  soc.sendto(mensagem.encode(), (host, porta))
  
  dados, servidor = soc.recvfrom(4096)
  dados = dados.decode()

  print(f"Cliente: {dados}")

finally:
  print("Fechando a conexão!")
  soc.close()