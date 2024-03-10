n = int(input("Digite a quantidade de números: "))

n1 = True
soma = 0

for i in range(n):
    while True:
        numero = int(input(f"Digite o número {i+1}: "))
        if 0 <= numero <= 1000:
            break
        else:
            print("Digite somente números entre 0 e 100")
    
    if n1:
        menor_valor = numero
        maior_valor = numero
        n1 = False
    else:
        if numero < menor_valor:
            menor_valor = numero
        if numero > maior_valor:
            maior_valor = numero
    
    soma += numero
    
print(f"Menor valor: {menor_valor}")
print(f"Maior valor: {maior_valor}")
print(f"Soma dos valores: {soma}")
