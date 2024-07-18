
# Contar de letras maiúsculas de minusculas 
def contarLetras(letter):
   tupe = tuple((i)for i in letter)
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


