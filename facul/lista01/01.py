n = int(input('Digite um número: '))

identificador = n % 2

if identificador == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')