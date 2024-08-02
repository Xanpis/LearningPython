
def nu():
    ite = int(input('INTEIRO = '))
    flo = float(input('FLUTUANTE = '))
    print(f'Números { ite} e {flo}')



# cap = True
# while(cap == True):
#     b = ''
#     try:
#         nu()
#     except Exception as ero:
#         print(f'Erro Valor invalido {ero.__cause__}')
#         b = ero.__cause__
#     if(b!= None):
#         cap == False


cap = True
while cap:
    try:
        nu()  # Chama a função que pode lançar uma exceção
        cap = False  # Sai do loop se `nu()` for executado sem erros
    except Exception as ero:
        print(f'Erro: Valor inválido - {str(ero)}')