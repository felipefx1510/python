import random
import time

num_g = random.randint(1,5)

num_u = int(input("Digite um número entre 1 e 5: "))

print("Processando...")
time.sleep(3)

if num_g == num_u:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você errou!\nO número era {num_g}")