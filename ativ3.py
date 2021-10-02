idade = int(input('Insira a idade do Gato: '))
castrado = input('O gato é Castrado (sim/não) ?')
sexo = input('Insira o sexo do gato (f/m): ')
fivFelv = input('Possui Fiv e Felv?(positivo/negativo): ')



if idade >= 0 and sexo == 'm' and fivFelv == 'positivo':

    print('SalaD')

elif idade >= 0 and fivFelv == 'positivo' and sexo == 'f':

    print('Fêmeas são alocadas  para outro gatil')

elif idade <= 2 and castrado == 'sim' or  sexo == 'm' and sexo == 'f' and castrado == 'não' and fivFelv == 'negativo':

    print('SalaA')

elif idade > 2 and castrado == 'sim':

    print('SalaB')

elif idade > 2 and castrado == 'não' and sexo == 'm':

    print('SalaC')