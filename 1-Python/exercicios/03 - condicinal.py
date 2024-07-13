
# num1 = int(input('Digite a quantidade em km = '))

# if num1 <= 200:
#    result = 0.5 * num1
# else:
#    result = 0.3 * num1

# print(f'O valor da sua viagem é R${result:.2f} ') 

salario = float(input('Qual seu salario para Aumento = '))

if salario <= 1250:
   aumento = salario + (salario * 0.15)
else:
   aumento = salario + (salario * 0.10) 

print(f'Seu novo salario é de R$ = {aumento} e teve um Aumento de {((aumento - salario) / salario) * 100 }% que foi de R$ = {aumento - salario}')