print('O questionário será rápido e direto...\n\n1. Digite "Sim" ou "Não" para as perguntas\n2. Após isso seu perfil será analisado para saber se você é suspeito, cúmplice ou assassino\n\nVamos começar!')

a = str(input('Telefonou para a vítima? ')).strip().upper()
b = str(input('Esteve no local do crime? ')).strip().upper()
c = str(input('Mora perto da vítima? ')).strip().upper()
d = str(input('Devia para a vítima? ')).strip().upper()
e = str(input('Já trabalhou com a vítma? ')).strip().upper()

print('Analisando seu perfil...')

resposta = [a, b, c, d, e]
print(f'{resposta}')
respostaresultado = resposta.count('SIM')