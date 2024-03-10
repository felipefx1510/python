print('Seja bem-vindo!')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

soma = n1 + n2

print(f'{n1} + {n2} = {soma}')

opcao = int(input('Deseja executar outra soma?\n1. Sim\n2. Não\n'))

while opcao == 1:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

    soma = n1 + n2

    print(f'{n1} + {n2} = {soma}')

    opcao = int(input('Deseja executar outra soma?\n1. Sim\n2. Não\n'))
    
else:
    print('Até mais!')