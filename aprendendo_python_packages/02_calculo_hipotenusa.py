import math

co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))

print(f'A hipotenusa é igual a: {math.hypot(co, ca):.2f}')