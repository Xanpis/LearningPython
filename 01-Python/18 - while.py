nameGame = input('Digite o nome do Jogo = ')

nota = 0
totalNota = 0
qetNota = 0

while (nota != -1):
   nota = float(input('Digite a nota = '))
   if (nota != -1):
      totalNota += nota
      qetNota += 1
print(f'Media das notas é = {totalNota / qetNota:.2f} do jogo {nameGame} ')

