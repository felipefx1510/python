n = int(input("Digite um número inteiro: "))

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            print(f"{n} não é um número primo.")
            break
    else:
        print(f"{n} é um número primo.")
else:
    print(f"{n } não é um número primo.")
