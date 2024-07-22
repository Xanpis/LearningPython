
# importando todo o arquivo
import calc

# importando apenas o método do arquivo
from calc import div

print(calc.sum(10,6))
print(calc.sub(10,6))
print(calc.mult(10,6))

# quando eu chamo não preciso informa o arquivo de onde vem na frente só chamo o método  
print(f'{div(10,6):.2f}')