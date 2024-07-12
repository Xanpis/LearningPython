
# Não é possível buscar valores via fatiamento o slice
gamesSet = {'Fifa', ' Star Wars', 'Mario Odyssey', 'Red Dead','Pes'}
print(gamesSet)

# No set e na tupla não se repete valores 
newGamesSet = {'God of war','Gta V','Fifa','true'}

# Adicionar um set a outro set
gamesSet.update(newGamesSet)
print(gamesSet)

# Remove mas só um de cada vez 
gamesSet.remove('true')
print(gamesSet)