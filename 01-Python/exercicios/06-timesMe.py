import os
# Variáveis  globais 
dicionario = {} 

# Adicionando um time
def adicionarTime():
   nome = input("Nome do time = ")
   dicionario[nome] = {'Time':nome,'Jogadores':[]}
   
      
# Adicionar jogadores
def adicionarJogador():
   numTime = int(input('Numero do Time para adicionar jogador = '))
   nomeTime = list(dicionario.keys())[numTime -1 ]
   if nomeTime in dicionario.keys():
      op = 's'
      while (op != 'n'): 
         nome = input('Digite o nome do jogador ou (n) para sair  = ')
         if nome != 'n':
            dicionario[nomeTime]['Jogadores'].append(nome)
         else:  
            op = 'n'
   else :
      print('Erro time')   
    


# Mostra Time
def mostrarTime():
   for ind ,(chave, valor) in enumerate(dicionario.items(), start = 1):
      # Imprimir com nome de jogadores 
      #   print(f'{ind}. {chave} = Jogadores = {join(valor['Jogadores'])} ')
         print(f'{ind}. {chave} : Jogadores = {len(valor['Jogadores'])} ')


# Mostra jogadores
def mostrarJogador(num):
   if num <= len(dicionario):
      nomeTime = list(dicionario.keys())[num -1]
      for i,jo in enumerate(dicionario[nomeTime]['Jogadores'], start = 1):
         print(f'{i}:{jo}')
   else:
      print('erro')
        

# Remover time
def rmvTime() :
   numTime = int(input('Digite o numero do Time a ser removido = '))
   if numTime <= len(dicionario):
     nomeTime = list(dicionario.keys())[numTime -1 ]
     del dicionario[nomeTime]
     print('Time removido!!!')
   else:
      print('erro')


# Remover jogador
def rmvJogador():
   numTime = int(input('Digite o numero do time para remover o jogador = '))
   mostrarJogador(numTime)
   if numTime <= len(dicionario):
     nomeTime = list(dicionario.keys())[numTime -1]
     numJoga = int(input('Numero do jogador a ser removido = '))
     if numJoga <= len(dicionario[nomeTime]['Jogadores']):
        del dicionario[nomeTime]['Jogadores'][numJoga -1]
     print('Jogador removido!!!')
   else:
      print('erro')


# Texto do menu
def shows():
   print(''' 
   Escolha uma das opções 

   (1) Adicionar um time
   (2) Adicionar jogador 
   (3) Listar times
   (4) Listar jogadores de um time
   (5) Remover um time
   (6) Remover jogador de um time
   (7) para sair   
   ''' )

# Menu
op = 9
while(op != 0):
   shows()
   try:
      op = int(input('Digite um dos números da Opção = '))
   except:
      print("Digite um Numero valido")   

   if op == 1:
      os.system('cls' if os.name == 'nt' else 'clear')
      adicionarTime()
    

   elif op == 2:
      os.system('cls' if os.name == 'nt' else 'clear')
      mostrarTime()
      adicionarJogador()

   elif op == 3:
      os.system('cls' if os.name == 'nt' else 'clear')
      mostrarTime()

   elif op == 4:
      os.system('cls' if os.name == 'nt' else 'clear')
      mostrarTime()
      num = int(input('Digite o numero do time para mostrar jogadores = '))
      mostrarJogador(num)

   elif op == 5:
      os.system('cls' if os.name == 'nt' else 'clear')
      mostrarTime()
      rmvTime()

   elif op == 6:
      os.system('cls' if os.name == 'nt' else 'clear')
      mostrarTime()
      rmvJogador()
      
   elif op == 7:
      op = 0
