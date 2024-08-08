import re
text = "He was carefully disguised butb captured quickly by police."
tu = re.findall(r"\w+r\b", text)

print(tu)