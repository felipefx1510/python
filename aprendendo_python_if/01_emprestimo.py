from time import sleep

print('Seja bem-vindo ao sistema de empréstimo!\nVamos começar!')
print('Carregando...')
sleep(2)

casa = float(input('Digite o valor da casa: '))
salario = float(input('Agora, digite o valor do seu salário mensal: '))
tempo = float(input('Para finalizarmos, por quantos anos você irá pagar o empréstimo? '))
print('Calculando...')
sleep(3)

emprestimo = casa / (tempo * 12)

if emprestimo >= salario*0.3:
    print('Infelizmente seu empréstimo não pode ser aprovado no momento.')
else:
    print('Parabéns, seu empréstimo foi aprovado!')