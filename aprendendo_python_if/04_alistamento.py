from datetime import date

print('Olá, seja bem-vindo!')

nascimento = int(input('Em que ano você nasceu? '))

anoatual = date.today().year

idadeatual = anoatual - nascimento

if idadeatual < 18:
    dif = 18 - idadeatual
    print(f'No momento você não poderá se alistar!\nAlistamento disponível em {dif} anos!')
elif idadeatual == 18:
    print(f'Alistamento disponível! Procure a Junta de Serviço Militar mais próxima!')
else:
    dif = idadeatual - 18
    print(f'Alistamento disponível! Alistamento encontra-se em atraso de {dif} anos!')
