km = int(input('Quantos km foram percorridos? '))
dias = int(input('Ficou quantos dias com o carro? '))

total = (km * 0.15) + (dias * 60)

print(f'O aluguel do carro encontra-se no valor de: R$ {total:.2f}!')