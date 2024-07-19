# Variáveis  globais 
dicionario = {} 

# Texto do menu
def shows():
   print(''' 
   Escolha uma das opções 

   (1) Adicionar um time
   (2) Adicionar jogador em um time
   (3) Listar times
   (4) Listar jogadores de um time
   (5) Remover um time
   (6) Remover jogador de um time    
   ''' )

# Adicionando um time

def adicionarTime():
   nome = input("Nome do time = ")
   dicionario[nome] = []
   print(dicionario)

# Adicionar jogador em um time
def adicionarJogador():
   nomeTime = input('Nome do time para add jogador = ')
   if nomeTime in dicionario.keys():
      nome = input("Nome do jogador = ")
      dicionario[nomeTime].append(nome)
      print(dicionario)
   else:
      print('Não temos este time na lista')

# Listar times 
def listarTimes():
   for i in dicionario.keys():
      print(f'\nTime = {i}')
  

# Listar Jogadores
def ListarJogadores():
   nomeTime = input('Nome do Time para lista jogadores = ') 
   if nomeTime in dicionario.keys():
      for i in dicionario[nomeTime]:
         print(f'\nJogadores = {i}')
   else:
      print('Não temos este time na lista')

# Remover um time
def removerTime():
   nome = input('Nome do Time Para Ser Removido = ')
   if nome in dicionario.keys():
      del dicionario[nome]
      print('Removido com sucesso!!!')
   else:
      print('O Time não existente')   

# Remover jogador de um time
def  removerJogador():
   nomeTime = input('Nome do time para remover jogador = ')
   if nomeTime in dicionario.keys():
      nomeJog = input('Digite o nome do jogador para ser removido ')
      for i in dicionario[nomeTime]:
         if nomeJog == i:
            dicionario[nomeTime].remove(i)

# Menu
op = 9
while(op != 0):
   shows()
   op = int(input('Digite a opção = '))
   if op == 1:
      adicionarTime()
   elif op == 2:
      adicionarJogador()
   elif op == 3:
      listarTimes()
   elif op == 4:
      ListarJogadores()
   elif op == 5:
      removerTime()
   elif op == 6:
      removerJogador()
      

   

  
