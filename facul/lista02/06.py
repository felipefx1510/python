print('O questionário será rápido e direto...\n\n1. Digite "Sim" ou "Não" para as perguntas\n2. Após isso seu perfil será analisado para saber se você é suspeito, cúmplice ou assassino\n\nVamos começar!')

a = str(input('Telefonou para a vítima? ')).strip().upper()
b = str(input('Esteve no local do crime? ')).strip().upper()
c = str(input('Mora perto da vítima? ')).strip().upper()
d = str(input('Devia para a vítima? ')).strip().upper()
e = str(input('Já trabalhou com a vítma? ')).strip().upper()

print('Analisando seu perfil...\n')

resposta = [a, b, c, d, e]
respostaresultado = resposta.count('SIM')

if respostaresultado < 2:
    print('Inocente!')
elif respostaresultado == 2:
    print('Suspeito!')
elif 2 < respostaresultado <= 4:
    print('Cúmplice!')
else:
    print('Assassino!')

