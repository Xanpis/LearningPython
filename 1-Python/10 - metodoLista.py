gameName = ["Resident evil 4", "Star wars Jedi survivor", 
"The Legend of Zelda", "Red dead 2", "Mario odyssey"]

# Tamanho da lista
print(len(gameName))

# Recuperar um índice de algo na lista 
print(gameName.index("Star wars Jedi survivor"))

# Adicionar item ao final da lista 
gameName.append( "Fifa 23")
print(gameName)

# Ordenar a lista 
gameName.sort()
print(gameName)

# Copiar lista
newGameName = gameName.copy()

# Remover item da lista
newGameName.remove("Fifa 23")
print(newGameName)

# Remover tudo da lista 
newGameName.clear()
print(newGameName)