name =  input('Digite uma frase com letras repetidas\n')

char = name[0].lower()
newName = name.replace(char,'$')
gameName = char.upper() + newName[1:]
print(gameName)  

st1 = 'xyc'
st2 = 'abz'

newSt1 =  st2[:2] + st1[2:]
print(newSt1)
newSt2 =  st1[:2] + st2[2:]
print(newSt2)