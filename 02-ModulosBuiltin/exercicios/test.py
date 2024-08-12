import re
# pegando a palavra inteira de um conjunto de string
text = "He was carefully disguised butb captured quickly by police."
tu = re.findall(r"\w+e \b", text)
print(tu)

