asteroides={}
asteroides['nome1'] = str(input('Digite o nome do asteoride 1: '))
asteroides['nome2'] = str(input('Digite o nome do asteroide 2: '))
asteroides['nome3'] = str(input('Digite o nome do asteroide 3: '))
distancias_asteroide1 = []
distancias_asteroide2 = []
distancias_asteroide3 = []
print('Digite as ultimas distância do asteroide {} da Terra'.format(asteroides['nome1']))
for x in range(1,6):    
    distancia = int(input('Digite a {}ª distancia que o asteroide esteve da Terra: '.format(x)))   
    distancias_asteroide1.append(distancia)
    print(distancias_asteroide1)
print('Digite as ultimas distância do asteroide {} da Terra'.format(asteroides['nome2']))
for x in range(1,6):    
    distancia = int(input('Digite a {}ª distancia que o asteroide esteve da Terra: '.format(x)))    
    distancias_asteroide2.append(distancia)
print(distancias_asteroide2)
print('Digite as ultimas distância do asteroide {} da Terra'.format(asteroides['nome3']))
for x in range(1,6):    
    distancia = int(input('Digite a {}ª distancia que o asteroide esteve da Terra: '.format(x)))    
    distancias_asteroide3.append(distancia)
    print(distancias_asteroide3)
asteroides['distancia1'] = distancias_asteroide1
asteroides['distancia2'] = distancias_asteroide2
asteroides['distancia3'] = distancias_asteroide3
asteroides['media1'] = sum(distancias_asteroide1) / 5
asteroides['media2'] = sum(distancias_asteroide2) / 5
asteroides['media3'] = sum(distancias_asteroide3) / 5
print('A distancia média do asteroide {} foi de {}km'.format(asteroides['nome1'],asteroides['media1']))
print('A distancia média do asteroide {} foi de {}km'.format(asteroides['nome2'],asteroides['media2']))
print('A distancia média do asteroide {} foi de {}km'.format(asteroides['nome3'],asteroides['media3']))