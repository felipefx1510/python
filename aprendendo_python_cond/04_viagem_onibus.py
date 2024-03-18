dist = int(input('Digite a distância da viagem em km: '))

if dist <= 200:
    preco = dist * 0.5
    print(f'O preço da passagem é R${preco:.2f}')
else:
    preco = dist * 0.45
    print(f'O preço da passagem é R${preco:.2f}')