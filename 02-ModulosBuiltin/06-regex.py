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
