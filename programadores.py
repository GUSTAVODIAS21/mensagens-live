def reply(ask):
    return eval(ask)

print('Programa para cálculos:')
print('Digite um cálculo matemático para obter o resultado')
print('  exemplo: 2 + 2 ')
while(True):
    ask = input('Digite uma expressão matemática: ')
    print  ('O resultado é : ', reply(ask))
