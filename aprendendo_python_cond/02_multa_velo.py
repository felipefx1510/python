velocidade = int(input('Digite a velocidade do carro: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Sua multa foi de R${multa:.2f}!')
else:
    print('Veículo dentro do limite de velocidade!')