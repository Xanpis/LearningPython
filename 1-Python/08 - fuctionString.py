
gameName = "fifa 2023"
description = """
   Fifa is a game development for Ea sports 
   you can ply online or not
"""
# retornar letras maiúsculos
print(gameName.upper()) 

#retorna letras minusculas
print(gameName.lower())

# primeira letra em maiúsculo
print(gameName.title())

# centralizando caractere,1 a quantidade de caractere, 2 o que vai ser preenchido  
print(gameName.center(11,"-"))

# Encontrando e retornado a posição do caractere 
print(gameName.find("a"))

# Contando números de caractere
print(description.count("a"))

# Alterando um string por outro string
print(description.replace("Fifa","Pes"))  

# Quebrando texto com ponto ou virgula
print(description.split(","))