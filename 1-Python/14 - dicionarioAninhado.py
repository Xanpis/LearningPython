import pprint

gameDict = {
   'Resident Evil 4':{
      'YearLaunch' : 2023,
      'Classification': 9.3,
      'Genre': ['ação', 'aventura'],
   },

   'Mario Odyssey ':{
      'YearLaunch' : 2020,
      'Classification': 8.2,
      'Genre': ['aventura','3d'],
   },

   'Donkey Kong country':{
      'YearLaunch' : 2021,
      'Classification': 7.8,
      'Genre': ['aventura','plataforma'],
   }
}

pp = pprint.PrettyPrinter(depth = 4)
pp.pprint(gameDict)

# Buscando valores no dicionario aninhado 
print(gameDict['Resident Evil 4']['Genre'])

# Adicionar items 
gameDict['Mario Odyssey ']['plays'] = 1 
print(gameDict['Mario Odyssey '])


# Excluir Dicionario 
del gameDict['Resident Evil 4']

del gameDict['Mario Odyssey ']['Genre']


pp.pprint(gameDict)

