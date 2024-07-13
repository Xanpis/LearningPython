gameList = ['Fifa','God of war','Red Dead','Mario Odyssey']

# Iteração com o for 
for game in gameList :
   print(game)
print(30 * '=')

# Break quando chega no valor determinado para 
for game in gameList:
   if game == 'Red Dead':
      break
   print(game)     
print(30 * '=')

# Continue chega até o valor especificado, pula e continua  
for i in gameList:
   if i == 'Red Dead':
      continue
   print(i)
print(30 * '=')

# Avaliação de um jogo
name = input('Digite o nome do jogo = ')
qtAvalia = int(input('Digite a quantidade de avaliação = '))

soma = 0 

for i in range(qtAvalia):
   nota = float(input('Digite a nota = '))
   soma += nota
print(f'A media das notas é {soma/qtAvalia}')
 