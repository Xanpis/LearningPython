# Calculo percentual de imposto
def calculo(sal ):
   if (sal < 1100):
      sal -= (sal * 0.5)
      return sal
   elif (sal < 2500):
      sal -= (sal * 0.10)
      return sal
   else:
      sal -= (sal * 0.15)
      return sal

sal = float(input('Digite o Salario = ')) 
adi = float(input('Digite o Adicional = '))
retor = calculo(sal)
print(f'\nDesconto de {((sal - retor)/sal)*100:.2f}% Em R${sal:.2f} Que foi de R${sal - retor:.2f} Valor total com Adicional é de R${retor + adi:.2f} ')
   