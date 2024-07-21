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
         print(f'{ind}. {chave} = Jogadores = {len(valor['Jogadores'])} ')
        
# Adicionando um time
def adicionarTime():
   nome = input("Nome do time = ")
   dicionario[nome] = {'Time':nome,'Jogadores':[]}
   # print(dicionario)

# Adicionar jogador em um time
def adicionarJogador():
   mostrarTime()
   numTime = int(input('Digite a posição do time  = '))
   nomeTime = list(dicionario.keys())[numTime -1 ]
   if nomeTime in dicionario.keys():
      nome = input('Digite o nome dos jogadores = ')
      dicionario[nomeTime]['Jogadores'].append(nome)
   else :
      print('noo tem')   



adicionarTime()  
adicionarTime()  
adicionarJogador()
adicionarJogador()
mostrarTime()

  