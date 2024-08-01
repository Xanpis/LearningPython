
def nu():
    ite = int(input('INTEIRO = '))
    flo = float(input('FLUTUANTE = '))
    print(f'Números { ite} e {flo}')


cap = True
while(cap == True):

    try:
        nu()
    except Exception as ero:
        print(f'Erro Valor invalido {ero.__cause__}')
        if(ero.__cause__!= None):
            cap == False
    