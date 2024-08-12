import random

# Sorteando número aleatório
list = [1,2,3,4,5]
print(random.choice(list))

# Gerando valor aleatório  
r1 = random.randint(1,60)
print(r1)

# Caractere de uma string aleatório
name = 'AprendendoPython'
r2 = random.choice(name)
print(r2)

# Selecionar mais de um valor aleatório de uma lista
print(random.sample(list, 3))

# Selecionando string aleatória 
s = "Hello world"
print(random.sample(s,4))
