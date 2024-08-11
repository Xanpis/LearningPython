import json

# Transformado string em dicionario
pessoa = '{"name": "Maria","languages":["Python","JavaScript"]}'
pessoa_dict = json.loads(pessoa)
print(pessoa_dict)
print(pessoa_dict['languages'])

# Convertendo dicionario para json
pessoa_json = json.dumps(pessoa_dict)
print(pessoa_json)
print(type(pessoa_dict))
print(type(pessoa_json))

# Imprimindo no Formato json
print(json.dumps(pessoa_dict, indent=4, sort_keys=True))

# Salvando txt 
with open('pessoa.txt','w') as file:
   json.dump(pessoa_dict,file)


# Abrindo aquivo json
with open('iris.json', 'r') as f:
   data = json.load(f)
   print(data)
