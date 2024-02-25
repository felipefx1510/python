nome = input('Digite seu nome: ')

print(f'Quantidade de A: {nome.upper().count('A')}')
print(f'Primeira letra A: {nome.upper().find('A') + 1}')
print(f'Última letra A: {nome.upper().rfind('A')}')