num1 = float(input('Digite um numero = '))
num2 = float(input('Digite um numero = '))
operator = input('Digite uma das operações (- + * /)')

if operator == '-':
   result = num1 - num2

elif operator == '+':
   result = num1 + num2

elif operator == '*':
   result = num1 * num2

elif operator == '/':
   result = num1 / num2
else:
   print('Não foi possível faze a operação ')

print(f'Resultado é = {result:.2f}')