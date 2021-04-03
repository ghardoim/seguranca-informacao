import itertools

string = input("Digite: ")
resultado = itertools.permutations(string, len(string))

for char in resultado:
  print("".join(char))