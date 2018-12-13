def soma( a, b):
    return a + b

def subtrai(a, b):
    return a - b

def mult(a, b):
    return a * b

def divisao(a, b):
    return a / b

print('Programa para calculos simples')
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um outro numero: '))
print('Os numero digitados foram: %.2f e %.2f' % (num1, num2))
print('Soma: %.2f' % soma(num1, num2))
print('Subtracao: %.2f' % subtrai(num1, num2))
print('Multiplicação: %.2f' % mult(num1, num2))
print('Divisao: %.2f' % divisao(num1, num2))
