from random import randint
from time import sleep

user = str(input('Digite se você quer pedra, papel ou tesoura: ')).upper()
pc = randint(1, 3)
print('Pedra!')
sleep(0.5)
print('Papel!')
sleep(0.5)
print('Tesoura!')
sleep(0.5)
if user == 'PEDRA':
    if pc == 1:
        print('Pedra -- Empate!')
    elif pc == 2:
        print('Papel -- Você perdeu!')
    else:
        print('Tesoura -- Você ganhou!')
elif user == 'PAPEL':
    if pc == 1:
        print('Pedra -- Você ganhou!')
    elif pc == 2:
        print('Papel -- Empate!')
    else:
        print('Tesoura -- Você perdeu!')
elif user == 'TESOURA':
    if pc == 1:
        print('Pedra -- Você perdeu!!')
    elif pc == 2:
        print('Papel -- Você ganhou!')
    else:
        print('Tesoura -- Empate!')
else:
    print('Opção digitada inválida!')