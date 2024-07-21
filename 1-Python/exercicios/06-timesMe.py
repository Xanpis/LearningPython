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


# Mostra Time
def mostrarTime():
   for ind ,(chave, valor) in enumerate(dicionario.items(), start = 1):
      # #  Imprimir com nome de jogadores 
      #   print(f'{ind}. {chave} = Jogadores = {join(valor['Jogadores'])} ')
         print(f'{ind}. {chave} : Jogadores = {len(valor['Jogadores'])} ')
        
# Adicionando um time
def adicionarTime():
   nome = input("Nome do time = ")
   dicionario[nome] = {'Time':nome,'Jogadores':[]}

# Adicionar jogador em um time
def adicionarJogador():
   mostrarTime()
   numTime = int(input('Numero do Time  = '))
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



adicionarTime()  
adicionarTime()  
adicionarJogador()
adicionarJogador()
mostrarTime()

  