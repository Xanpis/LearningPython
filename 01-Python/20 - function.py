
def cadastraGame():
   name =  input('Nome do jogo = ')
   # o Método retorna algo, não altera a original  
   name = name.title()
   price = input('Price R$ = ')
   print(f'{name} R$ {price}')
   print(25*'=')

cadastraGame()
cadastraGame()


