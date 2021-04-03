import hashlib

string = input("Digite: ")
string = string.encode("utf-8")

menu = int(input(''' ### MENU - ESCOLHA UM TIPO DE HASH ###
    1) MD5
    2) SHA1
    3) SHA256
    4) SHA512           
    \nEscolha: '''))

match menu:
  case 1:
    resultado = hashlib.md5(string)
  case 2:
    resultado = hashlib.sha1(string)
  case 3:
    resultado = hashlib.sha256(string)
  case 4:
    resultado = hashlib.sha512(string)

print(f"Hash: {resultado.hexdigest()}")