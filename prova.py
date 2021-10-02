pergunta=input('Deseja iniciar a contagem dos valores dos produtos ?(S/N):')
valor_total = 0 
while pergunta == 'S':
    valor_produto= float(input('Digite o valor do produto R$ '))
    valor_total=valor_total+valor_produto
    pergunta= input('Deseja  acrescenta mais produto ?(S/N):') 
    if pergunta == 'S': pass
    print('R$',valor_total) 
    faltante = 200 - valor_total >= 200
    print('eba Parabens voce atingiu o valor minimo e agora obteve o frete gratis! ')
    
else: 
 valor_total < 200
print ('oh ,ainda faltaram R$', faltante, 'para obter o frete gratis')
    

