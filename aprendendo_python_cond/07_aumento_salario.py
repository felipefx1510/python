salario = float(input('Digite o salário do funcionário: '))

if salario > 1250:
    aumento = salario + (salario * 0.1)
    print(f'O salário corrigido com 10% é de {aumento:.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'O salário corrigido com 15% é de {aumento:.2f}')