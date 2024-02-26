turno = str(input('Qual é o seu turno?\nM = Matutino\nV = Vespertino\nN = Noturno\n')).strip()

if turno.upper() == 'M':
    print('Bom dia!')
    
elif turno.upper() == 'V':
    print('Boa tarde!')
    
elif turno.upper() == 'N':
    print('Boa noite!')
    
else:
    print('Valor inválido!')