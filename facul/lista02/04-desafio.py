nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
salario = float(input("Digite seu salário: "))
sexo = input("Digite seu sexo - F ou M: ").upper()
estado_civil = input("Digite seu estado civil ('S', 'C', 'V' ou 'D'): ").upper()

if len(nome) <= 3:
    print("Nome inválido. O nome deve ter mais de 3 caracteres")
elif idade < 0 or idade > 150:
    print("Idade inválida. A idade deve ser entre 0 e 150")
elif salario <= 0:
    print("Salário inválido. O salário deve ser maior que 0")
elif sexo != 'F' and sexo != 'M':
    print("Sexo inválido. Digite 'F' ou 'M'")
elif estado_civil not in ['S', 'C', 'V', 'D']:
    print("Estado civil inválido. Digite: 'S', 'C', 'V' ou 'D'")
else:
    print("Tudo certo!")
