import hashlib

# Verificado algorítimos disponível para criptografia
print(hashlib.algorithms_available)

# verificando disponíveis para o sistema
print(hashlib.algorithms_guaranteed)

# Criptografando em sha256
print('Criptografia SHA266\n')
mensagem = 'A melhor maneira de prever o futuro é criando'.encode()
sha = hashlib.sha256()
print(sha.digest())
sha.update(mensagem)
print(sha.hexdigest())


# Criptografando em md5
print('Criptografia MD5\n')
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())