from collections import Counter,namedtuple,deque
from operator import itemgetter


# Contar items de uma lista 
fruits = [ 'Maçã','Manga','Tangerina', 'Banana','Uva','Melão',
 'Manga','Uva','Maçã','Manga','Tangerina','Uva','Banana']

print(fruits)
print(Counter(fruits))

# Utilizando tupla nomeada 
game = namedtuple('game',['nome','price','nota'])
g1 = game("Fifa23", 40, 5.0)
g2 = game("resident Evil 4 ", 97.90, 4.0)

print(g1)
print(g2)

# Ordenando dicionario
students = {'Pulo':23, 'Marcelo':34, 'Nadia':17, 'João':56, 'Ana':54, 'Maria':60}
a = sorted(students.items(),key=itemgetter(0))
print(students)
print(a)

# Utilizando filas ambas as extremidades
