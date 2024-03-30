nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('O aluno está reprovado.')
elif media >= 5 and media <= 6.9:
    print('O aluno irá para a recuperação.')
else:
    print('O aluno está aprovado.')