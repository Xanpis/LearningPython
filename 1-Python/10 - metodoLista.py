
gameLista = ["Resident evil 4", "Star wars Jedi survivor", 
"The Legend of Zelda", "Red dead 2", "Mario odyssey"]

# Tamanho da lista
print(len(gameLista))

# Recuperar um índice de algo na lista 
print(gameLista.index("Star wars Jedi survivor"))

# Adicionar item ao final da lista 
gameLista.append( "Fifa 23")
print(gameLista)

# Ordenar a lista 
gameLista.sort()
print(gameLista)

# Copiar lista
newGameLista = gameLista.copy()

# Remover item da lista
newGameLista.remove("Fifa 23")
print(newGameLista)

# Remover tudo da lista 
newGameLista.clear()
print(newGameLista)
