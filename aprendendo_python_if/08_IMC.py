peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do peso ideal!')
    
elif imc >= 18.5 and imc <= 25:
    print('Sua condição é normal!')
    
elif imc >= 25 and imc <= 30:
    print('Sua condição é de sobrepeso!')
    
elif imc >= 30 and imc <= 40:
    print('Sua condição é de obesidade!')
    
else:
    print('Sua condição é de obesidade mórbida!')