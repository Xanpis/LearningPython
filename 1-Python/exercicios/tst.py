# gameName = ["Resident evil 4", "Star wars Jedi survivor", 
# "The Legend of Zelda", "Red dead 2", "Mario odyssey"]

# # line = "="
# print(gameName[:-2])
# # print(line * 25)

# # name = "teste12"

# # print(gameName[::-2])

# # listaJogos = "Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"
# # print (lista) Jogos-1



def string_para_tuplas(s):
    tuplas = list((letra) for letra in s)
    print(tuplas)
    CPTL =  s.upper()
    for i in range(len(s)): 
      for f in tuplas[i]: 
         print(f)
         if (f in CPTL): 
            print('ok')
  
# Exemplo de uso:
string_para_tuplas("exemplo")