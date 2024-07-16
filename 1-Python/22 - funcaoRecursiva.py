
def fatorial (num):
   if num == 1 :
      return (1)
   else:
      # E como se fosse, num * a própria função -1, num guarda o valor acumulado e retorna depois 
      return(num * fatorial(num -1)) 

number  = int(input('Digite o fatorial = '))    
print(f'O fatorial de = {number} é = {fatorial(number)}')