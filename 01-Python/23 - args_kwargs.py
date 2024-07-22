
# Args os valores pagados viram uma tupla 

def soma(*num):
   totalSoma = 0
   for i in num:
      totalSoma += i
   print(f'Total das somas = {totalSoma}')   

soma(25,25,25)
print(25 * '=')


# kwargs os valores pagados viram um dicionario

def categoriaJogos(**categoria):
   for keys ,valor in categoria.items() :
      print(f' {keys}  {valor}')

categoriaJogos(Nome = 'Red Dead', Categoria = 'Ação', Idade = 18 )
categoriaJogos(Nome = 'Mario Odyssey', Categoria = 'Aventura', Idade = 18 )

