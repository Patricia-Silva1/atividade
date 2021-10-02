import math
ano = int(input('Digite um ano:'))
def validarSeculo(ano):
 return math.ceil(ano/100 )    

seculo = validarSeculo(ano)
print('Bem vindo ao seculo {}'.format(seculo))

def converter_inteiro_romano(inteiro):
    numero=[100,900,500,100,90,50,40,30,20,10,9,5,4,1]
    romanos=['M','CM','D','CD','C','XC','L','XL','X','IX','V''IV','I']

    numeral=''
    i=0

    while inteiro > 0:
     for _ in range(inteiro//numero[i]):
         numeral += romanos[i]
    inteiro -= numero [i]


    i+= 1

    return numeral
    print ('Bem vindo ao seculo {}'.format(converter_inteiro_romano(seculo)))
