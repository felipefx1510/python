subtotal = float(input('Digite o valor: '))
print('Formas de pagamento:\n1. À vista (dinheiro/cheque) - 10% de desconto\n2. À vista (cartão) - 5% de desconto\n3. até 2x (cartão)\n4. 3x ou mais - 20% de juros')
forma = int(input('Escolha a opção: '))

if forma == 1:
    total = subtotal - (subtotal * 0.1)
    print(f'O preço final é: R$ {total:.2f}')
elif forma == 2:
    total = subtotal - (subtotal * 0.05)
    print(f'O preço final é: R$ {total:.2f}')
elif forma == 3:
    total = subtotal
    print(f'O preço final é: R$ {total:.2f}')
elif forma == 4:
    total = subtotal + (subtotal * 0.2)
    print(f'O preço final é: R$ {total:.2f}')
else:
    print('Opção inválida!')