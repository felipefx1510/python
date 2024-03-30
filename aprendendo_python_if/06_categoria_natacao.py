from datetime import datetime

nascimento = int(input('Em que ano você nasceu? '))

idade = datetime.now().year - nascimento

if idade <= 9:
    print('Sua categoria é: MIRIM')
    
elif idade >= 10 and idade <= 14:
    print('Sua categoria é: INFANTIL')
    
elif idade >= 15 and idade <= 19:
    print('Sua categoria é: JUNIOR')
    
elif idade == 20:
    print('Sua categoria é: SÊNIOR')
    
else:
    print('Sua categoria é MASTER')
    
