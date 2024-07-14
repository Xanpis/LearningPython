
# for i in range(10):
#    if (i < 4 ):
#       print(i)

# Mesmo que o for mas com comprehension


preList = [i for i in range(10) if 1 < 4 ]
# print(preList)

# Verificando se há a letra a na lista
gameList = ['Mario Odyssey', 'Dk country', 'Luigi Mansion', 'Kirby']
newList = [x for x in gameList if 'a' in x ]
# print(newList)

tu = []
for i in gameList:
   if 'a' in i:
     tu.append(i)
print(tu)