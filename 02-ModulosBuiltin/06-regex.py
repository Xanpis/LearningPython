import re

text = 'Transformando pessoas em programadores sem limites'

# Índice inicial e final da apalavra, (r) quer dizer string bruta
mat = re.search(r'pessoas',text) 
print('inicial = ',mat.start())
print('final = ',mat.end())

# Buscando um ponto no site tem que colocar (\) para buscar corretamente
site = 'http://www.google.com'
found = re.search(r'\.',site)
print(found)

# buscando uma lista de caractere dentro de uma frase, buscando de (a até m) no alfabeto 
text = 'Transformando pessoas em programadores sem limites'
pad = "[a-m]"
result = re.findall(pad,text)
print(text)
print(result)

# buscando a primeira letra 
find = r'^A'
phrase = ['A casa está limpa','O dia começou lindo ', 'Vamos passear']
for f in phrase:
   if re.match(find,f):
      print("Corresponde = ",f)
   else:
      print('Nao Corresponde = ',f)

# verificando se tem no final de uma string
find = r'!$'
phrase2 = 'vagabond!'
result = re.search(find,phrase2)
if result:
   print('Contem')
else:
   print('Não tem')