import math

angulo = float(input('Digite o ângulo: '))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print(f'O seno do ângulo {angulo} é {sen:.2f}!')
print(f'O cosseno do ângulo {angulo} é {cos:.2f}!')
print(f'A tangente do ângulo {angulo} é {tg:.2f}!')