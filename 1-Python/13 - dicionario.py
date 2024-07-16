gameDict = {
   'name': 'Fifa',
   'years': 2023,
   'gamePrice': 99.20,
   'classification': 8.1,
   'genre':['Esporte', 'Familia']
}

print(gameDict)
print(len(gameDict))
print(type(gameDict))

# Recuperando valores 
print(gameDict['genre'][1])
print(gameDict.get('name'))

# Buscando apenas as chaves 
print(gameDict.keys())

# Buscando apenas valores 
print(gameDict.values())

# Buscando chaves e valores 
print(gameDict.items())

# Adicionar items no dicionario
gameDict['players'] = 2
print(gameDict)

# Atualizando valores do dicionario
gameDict.update({'players': 2 })
print(gameDict)

# Removendo valores
gameDict.pop('players') 
print(gameDict)
