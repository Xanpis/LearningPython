import random

r1 = random.randint(1,10)
done = False

while not done: 
   try:
      user = int(input('Escolha um numero ente 1 - 10 = '))
   except:
      pass

   if user == r1:
      print('Você acertou!!!!!')
      done = True
   else:
      print('Quase Acertou tente noma mente ')
   