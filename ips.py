import ipaddress

ip_1 = "192.168.0.1"
endereco = ipaddress.ip_address(ip_1)
print(endereco)

ip_2 = "192.168.0.100/24"
rede = ipaddress.ip_network(ip_2, strict = False)
for ip in rede:
  print(ip)