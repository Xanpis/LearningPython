
name = input('Digite o nome do joga = ')
yearsLaunch = int(input('Ano de lançamento = '))
classification = float(input('Classificação = '))

if classification > 8.0 or yearsLaunch >= 2015 :
   print(f'A recomendação do  jogo {name} é maior que que 8.0 ou ano {yearsLaunch} é maior que 2015')

else :
   print(f'Jogo {name} é mau avaliado ou data de lançamento é antiga ')

