import statistics

# 1- Media
print(statistics.mean([2,5,7,8,4,9]))

# 2 - Mediana (ordena o numero e pega o do meio)
print(statistics.median([3,5,7,10,10,12,16,17]))

# o numero que mais se repete é a moda 
print(statistics.mode([6,7,8,7,9,8,]))

# verificando o desvio padrão quanto mas perto de (0) melhor
print(statistics.stdev([1,3.5,5,1.2,1,2,3]))