n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1+n2)/2

if media == 10:
    print('Aluno aprovado com distinção!')

elif media >= 7 and media <= 9.99:
    print('Aluno aprovado!')
    
elif media >= 0 and media < 7:
    print('Aluno reprovado!')
    
else:
    print('NOTAS INCORRETAS!')
    