
total = 0
while True:
    produto = float(input('Insira o valor do produto R$:'))
    total+= produto
    
    resposta = input ("Voce deseja continuar comprando:[S/N]").upper()

    
        
    if total > 200:
                print ('O total  de compras foi de {:.2f}'.format(total))
                print ('eba parabens seu frete é gratis')

    else:
                print('o total  de compras de foi de {:.2f}'.format (total))
                print('O valor do frete é de {:.2f} '.format ((total * 2) /100))
 



    