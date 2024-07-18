# gameName = ["Resident evil 4", "Star wars Jedi survivor", 
# "The Legend of Zelda", "Red dead 2", "Mario odyssey"]

# # line = "="
# print(gameName[:-2])
# # print(line * 25)

# # name = "teste12"

# # print(gameName[::-2])

# # listaJogos = "Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"
# # print (lista) Jogos-1



# def string_para_tuplas(s):
#     tuplas = list(s)
#     print(tuplas)
#     CPTL =  s.upper()
#     for i in range(len(s)): 
#       for f in tuplas[i]: 
#          print(f)
#          if (f in CPTL): 
#             print('ok')
  
# # Exemplo de uso:
# string_para_tuplas("exemplo")


# # Contando impar e par 
# def parImpar(*lista):
#    print(lista)
#    par = []
#    impar = []
#    for priList in lista:
#       for segList in priList:
#          if (segList % 2 == 0):
#             par.append(segList)
#          else:
#             impar.append(segList)       
#    return(par,impar)

# enter = 1
# listaNumero = [] 
# while (enter != 0):
#    enter = int(input('Digite Os Números ou 0 para Sai = '))
#    if (enter != 0):
#       listaNumero.append(enter)

# listaParImpar = parImpar(listaNumero) 
# print(f'\nNúmeros pares = {listaParImpar[0]} Números Impares = {listaParImpar[1]}')