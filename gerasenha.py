import random, string

tamanho = int(input("Digite o tamanho da senha a ser gerada: "))
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;:/?"
rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(tamanho)))