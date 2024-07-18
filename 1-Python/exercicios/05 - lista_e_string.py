
# # Contar de letras maiúsculas de minusculas 
def contarLetras(letter):
   # Posso fazer iterado ou não
   tupe = tuple((i) for i in letter) 
   cpt = letter.upper()
   maiu = 0
   minu = 0
   for i in tupe :
      if(i in cpt):
         maiu +=1
      else:
         minu += 1
   return (maiu,minu)

enter = input('Contador de letras, maiúscula e minusculas \n Frase =  ')
contado = contarLetras(enter)
print(f'Maiúsculas = {contado[0]}  Minusculas = {contado[1]}')
print(70 * '=')

# Contando impar e par 
def parImpar(lista):
   print(lista)
   par = []
   impar = []
   for i in lista:
      if (i % 2 == 0):
         par.append(i)
      else:
         impar.append(i)       
   return(par,impar)

enter = 1
listaNumero = [] 
while (enter != 0):
   enter = int(input('Digite Os Números ou 0 para Sai = '))
   if (enter != 0):
      listaNumero.append(enter)

listaParImpar = parImpar(listaNumero) 
print(f'\nNúmeros pares = {listaParImpar[0]} Números Impares = {listaParImpar[1]}')

