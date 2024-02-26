print('Seja bem-vindo ao sistema de Caixa!')

valor = float(input('Digite o valor do produto: '))

desconto = valor - (valor*0.15)

print(f'O valor do produto com 15% de desconto é R$ {desconto:.2f}, sendo R$ {valor*0.15:.2f} de desconto.')