ladoa = int(input('Digite o primeiro lado do triângulo: '))
ladob = int(input('Digite o segundo lado do triângulo: '))
ladoc = int(input('Digite o terceiro lado do triângulo: '))

if ladoa == ladob and ladoa == ladoc and ladob == ladoc:
    print('O triângulo é equilatéro!')
elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print('O triângulo é isósceles!')
else:
    print('O triângulo é escaleno!')