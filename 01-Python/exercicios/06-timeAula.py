

teames = {}
done = False

# Lista times 
def printTemes():
# o enumerate retorna o índice no array  
   for i,team in enumerate(teames.values()):
      print(f'{i+1}. {team['nome']} {len(team['players'])} jogadores')


# Adicionar times 
def addTime():
   team_name = input("Digite o nome do time = ")
   teames[team_name] = {'nome':team_name, 'players':[] }
   print('Time adicionado ')
   print(teames)

# remover time 
def removerTime():
   printTemes()
   team_num = int(input('Digite o numero do time = '))
   if team_num <= len(teames):
      team_name = list(teames.keys())[team_num -1]
      del teames[team_name]
      print('Time removido')
   else:
      print('Numero do time invalido ')

# Listar jogadores 
def printTimesPlayers(tem):
   print(f'Jogadores do {tem['nome']}')
   for i, player in enumerate(tem['players']):
      print(f'{i+1}.{player}')


#Adicionar jogadores 
def adicionarJogador():
   team_num = int(input('Digite o numero do time que deseja adicionar = '))
   if team_num <= len(teames):
      player_name = input("Informe o nome do jogador = ")
      team_name = list(teames.keys())[team_num -1]
      teames[team_name]['players'].append(player_name)
      print('jogador adicionado !!!')
   else:
      print('Nome do time esta invalido')

      
while not done:
   print('Q que deseja fazer')

   print('1. Adicionar time ')
   print('2. Remover time ')
   print('3. Listar times')
   print('4. Adicionar jogador ao time')
   print('5. Remover jogadores de um time')
   print('6. Listar jogadores do time ')
   print('7.Sair ')
  
   choice = int(input(">"))
   # O (pass) é parra esperar o resto do código 
   if choice == 1:
      addTime()
   elif choice == 2:
      pass
   elif choice == 3:
      printTemes()
   elif choice == 4:
      printTemes()
      adicionarJogador()
   elif choice == 5:
      printTemes()
      team_num = int(input('Digite o numero do time para remover jogador = '))
      if team_num <= len(teames):
        team_name = list(teames.keys())[team_num -1]
        printTimesPlayers(teames[team_name])
        player_num = int(input('Informe o nome do jogador que deseja remover = '))
        if player_num <= len(teames[team_name]['players']):
            del teames[team_name]['players'][team_num-1]
            print('Jogador Removido !!!')
      else:
         print('Numero do jogador invalido')   

   elif choice == 6:
      printTemes()
      team_num = int(input('Digite o numero do time = '))
      if team_num <= len(teames):
         team_name = list(teames.keys())[team_num -1]
         printTimesPlayers(teames[team_name])
      else:
         print('Numero do time invalido')    

   elif choice == 7:
      done = True
   else:
      print('Opção invalida')