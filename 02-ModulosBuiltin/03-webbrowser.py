import webbrowser

done = False

while not done:
   print('Escolha uma da Opções')
   print('1- Site python')
   print('2- Módulos python')
   print('3- Sair')

   op = input('> ')
   if op == '1':
      # Abrindo link web
      webbrowser.open('https://www.python.org/')
   elif op == '2':
      webbrowser.open('https://docs.python.org/3/py-modindex.html')
   elif op == '3':
      done = True
   else:
      print('Opção errada')

   